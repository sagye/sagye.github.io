from manim import *
import numpy as np

class Integral(VGroup):
    def __init__(
            self,
            axes, func,
            T=1.0, initial_bins=4,
            **kwargs,
    ):
        super().__init__(**kwargs)

        self.color_graph = "white"
        self.color_positive = "blue"
        self.color_negative = "red"

        self.axes = axes
        self.func = func
        self.T = T

        self.num_bins = ValueTracker(initial_bins)
        self.sample_ratio = ValueTracker(0)
        self.stretch_tracker = ValueTracker(0)

        self.reset_widths(initial_bins)

        # Visuals
        self.func_graph = always_redraw(self.stretch_graph)
        self.func_graph.set_z_index(10)

        self.rects = VGroup()
        for i in range(int(self.num_bins.get_value())):
            rect, _ = self.create_rect(i)
            self.rects.add(rect)
        self.rects.set_z_index(1)
        self.rects.add_updater(lambda m: self.update_rectangles())
        self.add(self.rects, self.func_graph)  # Ensure they are added to the VGroup


    def get_graph(self):
        return self.func_graph
    def get_rects(self):
        return self.rects
    def add_graph(self):
        self.add(self.func_graph)
    def add_rects(self):
        self.add(self.rects)
    def reset_widths(self, num_bins):
        # State: SIGNED Widths (for math/color)
        init_w = self.T / num_bins
        self.widths = np.ones(num_bins) * init_w
        self.widths_start = self.widths.copy()
        self.widths_target = self.widths.copy()

        # State: ABSOLUTE Widths (for visual positioning)
        self.abs_widths_start = np.abs(self.widths_start)
        self.abs_widths_target = np.abs(self.widths_target)

        # State: Fixed parameter partition [0, T]
        self.parameter_widths = np.ones(num_bins) * init_w
        self.param_partition = np.concatenate([[0], np.cumsum(self.parameter_widths)])

    def reset_rects(self):
        self.rects = VGroup()
        for i in range(int(self.num_bins.get_value())):
            rect, _ = self.create_rect(i)
            self.rects.add(rect)
        self.rects.set_z_index(1)
        self.rects.add_updater(lambda m: self.update_rectangles())

    def get_current_widths(self):
        """ Returns interpolated SIGNED widths. """
        alpha = self.stretch_tracker.get_value()
        return (1 - alpha) * self.widths_start + alpha * self.widths_target

    def get_current_abs_widths(self):
        """ Returns interpolated ABSOLUTE widths for layout. """
        alpha = self.stretch_tracker.get_value()
        return (1 - alpha) * self.abs_widths_start + alpha * self.abs_widths_target

    def stretch_x(self, t):
        """ Maps time t in [0, T] to the current stretched x-coordinate. """
        curr_abs_widths = self.get_current_abs_widths()
        visual_partition = np.concatenate([[0], np.cumsum(curr_abs_widths)])

        if t <= self.param_partition[0]: return visual_partition[0]
        if t >= self.param_partition[-1]: return visual_partition[-1]

        i = np.searchsorted(self.param_partition, t) - 1
        i = np.clip(i, 0, len(curr_abs_widths) - 1)

        local_alpha = (t - self.param_partition[i]) / (self.param_partition[i + 1] - self.param_partition[i])
        return interpolate(visual_partition[i], visual_partition[i + 1], local_alpha)

    def stretch_graph(self):
        points = [self.axes.c2p(self.stretch_x(t), self.func(t)) for t in np.linspace(0, self.T, 300)]
        graph = VMobject(color=self.color_graph, stroke_width=3)
        graph.set_points_smoothly(points)
        return graph

    def create_rect(self, i, value=None):
        # Get current states
        curr_signed_widths = self.get_current_widths()
        curr_abs_widths = self.get_current_abs_widths()

        visual_partition = np.concatenate([[0], np.cumsum(curr_abs_widths)])
        x_left = visual_partition[i]
        w_visual = curr_abs_widths[i]

        # Sample function height
        t_sample = interpolate(self.parameter_widths[i] * i, self.parameter_widths[i] * (i + 1),
                               self.sample_ratio.get_value())
        height = self.func(t_sample) if value is None else value

        # COLOR LOGIC -- Contribution = f(t) * ΔW. Positive product = Color #1, Negative = Color #2.
        is_positive = (height * curr_signed_widths[i]) >= 0
        color = self.color_positive if is_positive else self.color_negative

        # Visual Creation
        x_scale = self.axes.x_length / (self.axes.x_range[1] - self.axes.x_range[0])
        y_scale = self.axes.y_length / (self.axes.y_range[1] - self.axes.y_range[0])

        stroke_width = 1 if len(curr_signed_widths) <=20 else (2 / (len(curr_signed_widths) - 20))

        rect = Rectangle(
            width=w_visual * x_scale,
            height=abs(height) * y_scale,
            fill_color=color,
            fill_opacity=0.7,
            stroke_width=stroke_width,
            stroke_color="black",
        )

        # Anchor to the left and handle positive/negative Y
        rect.move_to(self.axes.c2p(x_left, 0), aligned_edge=LEFT)
        if height >= 0:
            rect.shift(UP * (abs(height) * y_scale / 2))
        else:
            rect.shift(DOWN * (abs(height) * y_scale / 2))

        return rect, [x_left + w_visual / 2, height / 2]

    def update_rectangles(self):
        for i in range(len(self.rects)):
            new_rect, _ = self.create_rect(i)
            self.rects[i].become(new_rect)

    def adjust_widths(self, new_widths):
        # Setup for animation: start = current; target = new
        self.widths_start = self.get_current_widths().copy()
        self.widths_target = np.array(new_widths).copy()

        self.abs_widths_start = np.abs(self.widths_start)
        self.abs_widths_target = np.abs(self.widths_target)

        self.stretch_tracker.set_value(0)

    def commit_widths(self):
        # seal the animation state
        self.widths_start = self.widths_target.copy()
        self.abs_widths_start = self.abs_widths_target.copy()
        self.stretch_tracker.set_value(0)

    def refine_bins(self, factor=2):
        old_rects = self.rects
        old_n = len(old_rects)
        new_n = old_n * factor

        # Logic Update
        self.parameter_widths = np.ones(new_n) * (self.T / new_n)
        self.param_partition = np.concatenate([[0], np.cumsum(self.parameter_widths)])

        # Split current signed widths
        curr_w = self.get_current_widths()
        new_w = []
        for w in curr_w:
            new_w.extend([w / factor] * factor)

        self.widths_start = np.array(new_w)
        self.widths_target = self.widths_start.copy()
        self.abs_widths_start = np.abs(self.widths_start)
        self.abs_widths_target = self.abs_widths_start.copy()

        # Visual update
        intermediate_rects = VGroup()
        transforms = []
        for i in range(old_n):
            t_p_start = i * (self.T / old_n)
            t_p_end = (i + 1) * (self.T / old_n)
            t_p_sample = interpolate(t_p_start, t_p_end, self.sample_ratio.get_value())
            parent_h = self.func(t_p_sample)

            children = VGroup()
            for j in range(factor):
                child_idx = i * factor + j
                rect, _ = self.create_rect(child_idx, value=parent_h)
                children.add(rect)
                intermediate_rects.add(rect)

            transforms.append(ReplacementTransform(old_rects[i], children))

        self.remove(self.rects)
        self.rects = intermediate_rects
        self.rects.set_z_index(1)
        self.add(self.rects)
        return AnimationGroup(*transforms)

    def get_height_adjustment(self):
        target_rects = VGroup()
        for i in range(len(self.rects)):
            rect, _ = self.create_rect(i)
            target_rects.add(rect)
        return Transform(self.rects, target_rects)



class IntegralDemo(Scene):
    def construct(self):
        # Axes
        axes = Axes(
            x_range=[0, 4, 1],
            y_range=[-1, 2, 1],
            x_length=7,
            y_length=4,
            axis_config={"include_tip": False},
        )

        self.add(axes)
        N = 4  # number of bins

        # First visualisation: deterministic integral
        func = lambda x: np.sin(x) + 0.5
        integral = Integral(axes, func, T=4, initial_bins=N,)
        self.play(FadeIn(integral))

        # Make rectangles react to sample point
        integral.add_updater(lambda m, dt: m.update_rectangles())

        # Refine partition
        integral.suspend_updating()
        self.play( integral.refine_bins(factor=2), run_time=0.8,)
        self.wait(0.3)
        # Height adjustment (rectangles move to their correct functional heights)
        self.play(integral.get_height_adjustment(), run_time=0.8)

        self.play(integral.refine_bins(factor=3), run_time=0.8, )
        self.play(integral.get_height_adjustment(), run_time=0.8)
        integral.resume_updating()
        self.wait(2)

        # Test evaluation point animation: left -> midpoint -> right -> left
        self.play(
            integral.sample_ratio.animate.set_value(0.5), run_time=1,
        )
        self.wait(0.2)

        self.play(
            integral.sample_ratio.animate.set_value(1), run_time=1,
        )
        self.wait(0.2)

        self.play(
            integral.sample_ratio.animate.set_value(0), run_time=1,
        )
        self.wait(0.2)


        # Gaussian increments
        bm = np.random.normal(loc=0, scale=1, size=N)
        bm = np.abs(bm)

        # Stretch integral according to Brownian increments
        increments = bm

        for i in range(10):
            widths = integral.get_current_widths().copy()
            widths[i] = increments[i]
            integral.adjust_widths(widths)

            self.play(
                integral.stretch_tracker.animate.set_value(1),
                run_time=0.5,
            )
            integral.commit_widths()


        # Force one rectangle height for testing purposes
        forced_height = 1.5

        i = 0
        rect, pos = integral.create_rect(i=i, value=forced_height,)

        rect.move_to(integral.axes.c2p(*pos))
        old = integral.rects[i]
        self.play(Transform(old, rect), run_time=2,)
        self.wait()