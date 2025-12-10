import gradio as gr

def bubble_sort_steps(arr):
    """
    Bubble Sort with clear step-by-step output.
    Returns a formatted string showing comparisons and swaps.
    """
    steps = []
    a = arr.copy()
    n = len(a)

    steps.append(f"Initial List: {a}")

    for i in range(n):
        swapped = False
        steps.append(f"\n--- Pass {i+1} ---")

        for j in range(0, n - i - 1):
            steps.append(f"Comparing {a[j]} and {a[j+1]}")

            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
                steps.append(f" → Swap → {a}")
            else:
                steps.append(" → No swap")

        if not swapped:
            steps.append("No swaps in this pass → list is already sorted.")
            break

        steps.append(f"End of Pass {i+1}: {a}")

    steps.append(f"\nFinal Sorted List: {a}")
    return "\n".join(steps)


def parse_list(text):
    """Convert comma-separated numbers into a Python list."""
    try:
        return [int(num.strip()) for num in text.split(",")]
    except:
        return None


def run_sort(text):
    arr = parse_list(text)
    if arr is None:
        return "❌ ERROR: Please enter comma-separated integers, e.g., 5, 2, 9, 1"
    return bubble_sort_steps(arr)


with gr.Blocks() as demo:
    gr.Markdown("""
    # 🫧 Bubble Sort Visual Simulation
    Enter a list of numbers to see how Bubble Sort works step-by-step.
    """)

    input_box = gr.Textbox(label="Enter comma-separated integers")
    output_box = gr.Textbox(label="Bubble Sort Steps", lines=25)

    run_button = gr.Button("Run Bubble Sort")
    run_button.click(run_sort, inputs=input_box, outputs=output_box)

if __name__ == "__main__":
    demo.launch()
