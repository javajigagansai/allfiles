from fpdf import FPDF
import matplotlib.pyplot as plt
import numpy as np

# Create diagram for asymptotic complexity
n = np.linspace(1, 10, 100)
best = np.ones_like(n)
average = n / 2
worst = n

plt.figure(figsize=(8, 5))
plt.plot(n, best, label='Ω(1) - Best Case', linestyle='--')
plt.plot(n, average, label='Θ(n) - Average Case', linestyle='-.')
plt.plot(n, worst, label='O(n) - Worst Case', linestyle='-')
plt.xlabel('Input Size (n)')
plt.ylabel('Time Complexity')
plt.title('Asymptotic Complexity Bounds')
plt.legend()
plt.grid(True)
diagram_path = "/mnt/data/asymptotic_complexity_diagram.png"
plt.savefig(diagram_path, bbox_inches='tight')
plt.close()

# Define PDF class
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "Asymptotic Analysis of Complexity Bounds", ln=True, align="C")
        self.ln(5)

    def chapter_title(self, title):
        self.set_font("Arial", "B", 12)
        self.cell(0, 8, title, ln=True)
        self.ln(1)

    def chapter_body(self, body):
        self.set_font("Arial", "", 11)
        self.multi_cell(0, 6, body)
        self.ln(2)

# Content for PDF
content = [
    ("Introduction",
     "In computer science, evaluating an algorithm's efficiency is essential for understanding its performance. "
     "This evaluation is often done using asymptotic analysis, which studies how the running time or space "
     "requirements grow with the input size n, especially as n becomes very large. It ignores machine-specific "
     "constants and focuses on general growth trends. The three major complexity bounds in asymptotic analysis are: "
     "Best-case, Average-case, and Worst-case behavior."),

    ("1. Best-Case Complexity (Ω-notation)",
     "Definition: The best-case complexity defines the minimum time or space an algorithm takes for any input of size n. "
     "Notation: Ω(f(n)).\n"
     "Example: In linear search, if the element is found at the first position, time complexity is Ω(1).\n"
     "Significance: Indicates the most optimistic scenario, but is less useful since it rarely occurs."),

    ("2. Average-Case Complexity (Θ-notation)",
     "Definition: Estimates the expected time or space an algorithm will take over all possible inputs of size n. "
     "Notation: Θ(f(n)).\n"
     "Example: In linear search, the average-case time complexity is Θ(n).\n"
     "Significance: Represents realistic performance under typical input distribution."),

    ("3. Worst-Case Complexity (O-notation)",
     "Definition: Defines the maximum time or space required for any input of size n. "
     "Notation: O(f(n)).\n"
     "Example: In linear search, if the element is not found, time complexity is O(n).\n"
     "Significance: Most commonly used as it guarantees performance will not exceed this bound."),

    ("Importance of Asymptotic Analysis",
     "• Machine independence: Focuses on algorithm logic, not hardware.\n"
     "• Scalability assessment: Predicts behavior with growing input.\n"
     "• Algorithm comparison: Enables objective efficiency comparison.\n"
     "• Resource planning: Estimates computational needs accurately."),

    ("Diagram",
     "The following diagram shows the relationship between input size and time complexity "
     "for best, average, and worst-case scenarios:")
]

# Create PDF
pdf = PDF()
pdf.add_page()

for title, body in content:
    pdf.chapter_title(title)
    pdf.chapter_body(body)

# Insert diagram image
pdf.image(diagram_path, x=15, w=180)

# Save PDF
final_pdf_path = "/mnt/data/Asymptotic_Analysis_16_Marks.pdf"
pdf.output(final_pdf_path)
final_pdf_path
