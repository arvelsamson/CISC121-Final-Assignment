# Interactive Bubble Sort Visualizer
**CISC 121 – Final Assignment**  
**Author:** Arvel Samson  

---

## Demo Screenshot  

https://github.com/user-attachments/assets/a1541530-1585-4348-a2d3-46e9ee8db25a

---

# Problem Breakdown & Computational Thinking

For this project, I chose **Bubble Sort** because it’s simple to understand and perfect for showing how a sorting algorithm works step-by-step. The goal was to make the process visual and interactive so users can actually see what the algorithm is doing at each stage.

To build the project, I broke the problem into smaller parts:

1. Let the user input a list of numbers.  
2. Determine the input and validate it.  
3. Sort the list using Bubble Sort.  
4. Show every comparison and swap.  
5. Make it interactive with buttons (Next Step, Auto-Run, Reset).  
6. Display everything clearly using Gradio.

---

# Decomposition

Here are the main components I identified:

- **Input handling:** Get numbers from the user and convert them into a list.  
- **Algorithm engine:** Run Bubble Sort one step at a time so the user can follow it.  
- **Visualization:** Highlight the numbers being compared and show swaps.  
- **Controls:** Start, Next Step, Auto-Run, and Reset buttons.  
- **UI:** Use Gradio to build a clean online interface.

---

# Pattern Recognition

Some patterns that helped build the program:

- Bubble Sort always compares **adjacent** values.  
- After each full pass, the largest value ends up at the end of the list.  
- If an entire pass happens with **no swaps**, the list is already sorted.  
- The amount of work reduces with each pass.

---

# Abstraction

To avoid overwhelming the user, I only show:

- The current state of the list  
- Which two numbers are being compared  
- When swaps happen  
- When a pass ends  
- A final sorted list  

Things like loop indexes, memory details, and internal state are hidden because they aren’t important to the user experience.

---

#Algorithm Design (Input → Process → Output)

### **Input**
The user types something like:
```
5, 3, 8, 1, 4
```

### **Process**
- Compare two numbers at a time  
- Swap if needed  
- Move through the list  
- Repeat until the list is sorted  
- Allow the user to move step-by-step or run automatically  

### **Output**
An easy-to-follow visualization that displays the output of the sorted list.
```
1, 3, 4, 5, 8
```

---

# Flowchart

<img width="1578" height="1856" alt="Image 2025-12-10 at 4 42 AM" src="https://github.com/user-attachments/assets/5fd2babf-201d-4828-b1fe-d8044fd075ce" />


---

# How to Run the Program

1. Access the Hugging Face link, posted under "Hugging Face Link". You can access the app from here
  
2. Once you open the app, enter the numbers you want to be sorted. These numbers should be separated by commas.

3. Click the "Start" button to start the sorting.

4. Click next to step (or auto run) through each comparison and swap.
   
5. Continue pressing next-step until the list is sorted.
   
6. Press reset after the list is sorted if the user wants to input another list.

---

# Testing & Verification

Here are some tests I used to confirm the program works:

| Input | Expected Result |
|-------|----------------|

| `5,4,3,2,1` | Many swaps until sorted |

https://github.com/user-attachments/assets/e393a8fc-ea9a-4b6e-b0da-b00687266727

| `1,2,3,4,5` | No swaps — ends early |

https://github.com/user-attachments/assets/425c4069-0045-46c6-9cb5-62249a118d80

| `8,3,5,1` | Sorted as `[1,3,5,8]` |

https://github.com/user-attachments/assets/b695e815-7a71-41da-aa00-10634c1ab799

| `17` | Single number, no changes |

https://github.com/user-attachments/assets/83a9e9f8-f50d-4098-abfe-2944d4772eaa

| `4, x, 9` | Error message |

https://github.com/user-attachments/assets/87644528-8cb3-422d-8ea2-be648b203a79

---

# Hugging Face Deployment  
https://huggingface.co/spaces/arvelsamson/BubbleSpace

---

# GitHub Repository  
[*(Add your GitHub project link here.)*]
(https://github.com/arvelsamson/CISC121-Final-Assignment)
---

# Summary

This project demonstrates:

- A complete Bubble Sort implementation  
- A clean visual explanation of each comparison and swap  
- Interactive controls using Gradio  
- Strong computational thinking practices  
- Clear documentation and testing  

# The End
