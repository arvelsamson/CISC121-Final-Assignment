import gradio as gr
import time

# ============================================
# BUBBLE SORT INTERACTIVE ENGINE
# ============================================

class BubbleSortEngine:
    def __init__(self, arr):
        self.original = arr[:]
        self.arr = arr[:]
        self.n = len(arr)
        self.i = 0
        self.j = 0
        self.finished = False
        self.swapped_in_pass = False

    def render_state(self, highlight=None, message=""):
        html = "<h3 style='color:#4A90E2;'>Current Array:</h3><p>"

        for idx, val in enumerate(self.arr):
            if highlight and idx in highlight:
                html += f"<span style='background:#FF474C; padding:4px; border-radius:5px; font-weight:bold;'>{val}</span> "
            else:
                html += f"<span style='font-size:18px'>{val}</span> "

        html += "</p>"
        if message:
            html += f"<p style='color:#27AE60; font-weight:bold;'>{message}</p>"

        return html

    def step(self):
        """Perform ONE step of Bubble Sort."""
        if self.finished:
            return self.render_state(message="🎉 Sorting complete!")

        # End of pass
        if self.j >= self.n - self.i - 1:
            if not self.swapped_in_pass:
                self.finished = True
                return self.render_state(message="✨ No swaps — list sorted!")
            # Otherwise move to next pass
            self.i += 1
            self.j = 0
            self.swapped_in_pass = False
            return self.render_state(message=f"🔁 Starting Pass {self.i + 1}")

        # Compare
        a, b = self.arr[self.j], self.arr[self.j + 1]

        msg = f"Comparing {a} and {b}"
        highlight = [self.j, self.j + 1]

        if a > b:
            # Swap
            self.arr[self.j], self.arr[self.j + 1] = b, a
            self.swapped_in_pass = True
            msg = f"🔄 Swap performed → {self.arr}"

        self.j += 1
        return self.render_state(highlight, msg)


# ============================================
# GLOBAL SESSION STORAGE
# ============================================

sessions = {}

def start_sort(user_input):
    try:
        arr = [int(x.strip()) for x in user_input.split(",")]
    except:
        return "<p style='color:red;'>❌ Invalid input. Enter numbers separated by commas.</p>"

    sessions["engine"] = BubbleSortEngine(arr)
    return sessions["engine"].render_state(message="🚀 Sorting started!")

def next_step():
    if "engine" not in sessions:
        return "<p style='color:red;'>❌ Start sorting first.</p>"
    return sessions["engine"].step()

def auto_run():
    if "engine" not in sessions:
        return "<p style='color:red;'>❌ Start sorting first.</p>"

    engine = sessions["engine"]
    final_html = ""

    while not engine.finished:
        final_html += engine.step() + "<hr>"
        time.sleep(0.15)

    final_html += "<h2 style='color:#27AE60;'>🎉 Finished!</h2>"
    return final_html

def reset_sort():
    sessions.clear()
    return "<p style='color:#757575;'>🔄 Reset complete. Enter a new list to start again.</p>"


# ============================================
# GRADIO UI
# ============================================

with gr.Blocks(theme=gr.themes.Soft()) as demo:

    gr.Markdown("""
    # 🫧 **Interactive Bubble Sort Simulator**
    A fun, interactive way to explore Bubble Sort with live updates, animations, and controls!

    👉 Enter numbers like: `5, 2, 9, 1, -6`
    """)

    input_box = gr.Textbox(label="Enter numbers (place comma after)")
    output_box = gr.HTML(label="Visualization Output")

    with gr.Row():
        start_btn = gr.Button("▶️ Start")
        next_btn = gr.Button("➡️ Next Step")
        auto_btn = gr.Button("⏩ Auto-Run")
        reset_btn = gr.Button("🔄 Reset")

    start_btn.click(start_sort, inputs=input_box, outputs=output_box)
    next_btn.click(next_step, outputs=output_box)
    auto_btn.click(auto_run, outputs=output_box)
    reset_btn.click(reset_sort, outputs=output_box)

demo.launch()
