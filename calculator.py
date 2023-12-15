import tkinter as tk  # Import the tkinter module for GUI

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")  # Set the title of the calculator window
        self.expression = ''  # Initialize expression to hold user input
        self.history = []  # Initialize a list to hold calculation history
        
        # Create the display entry widget for showing input and output
        self.create_display()
        # Create buttons for numbers, operations, clear, and equals
        self.create_buttons()
        # Create history display area to show past calculations
        self.create_history()

    def create_display(self):
        # Create an Entry widget for the display, where user input/output will be shown
        self.display = tk.Entry(self.root, width=30, font=('Arial', 14), bd=5, justify="right")
        self.display.grid(row=0, column=0, columnspan=4)  # Place the display at the top

    def create_buttons(self):
        # Define the buttons for the calculator
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        # Create buttons and assign commands based on button type
        for (text, row, column) in buttons:
            if text != '=' and text != 'C':
                button = tk.Button(self.root, text=text, width=5, height=2, font=('Arial', 12),
                                   command=lambda t=text: self.add_to_expression(t))
            elif text == '=':
                button = tk.Button(self.root, text=text, width=5, height=2, font=('Arial', 12),
                                   command=self.calculate)
            else:
                button = tk.Button(self.root, text=text, width=5, height=2, font=('Arial', 12),
                                   command=self.clear_display)
            button.grid(row=row, column=column)  # Place buttons in the grid layout

    def create_history(self):
        # Create a label for the history section
        self.history_label = tk.Label(self.root, text="History:", font=('Arial', 12))
        self.history_label.grid(row=5, column=0, columnspan=4)  # Place the label

        # Create a Text widget for displaying calculation history
        self.history_display = tk.Text(self.root, height=5, width=30, font=('Arial', 12))
        self.history_display.grid(row=6, column=0, columnspan=4)  # Place the history display area

    def add_to_expression(self, value):
        # Function to add the clicked button's value to the expression
        self.expression += str(value)
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)  # Show the updated expression in the display

    def clear_display(self):
        # Function to clear the display
        self.expression = ''
        self.display.delete(0, tk.END)

    def calculate(self):
        # Function to evaluate the expression and show the result
        try:
            result = eval(self.expression)  # Evaluate the expression using eval()
            self.history.append(self.expression + ' = ' + str(result))  # Add the calculation to history
            self.history_display.delete(1.0, tk.END)  # Clear previous history display
            # Show the last 5 calculations in the history display area
            self.history_display.insert(tk.END, '\n'.join(self.history[-5:]))
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, result)  # Show the result in the display
            self.expression = str(result)  # Update expression to result for further calculations
        except Exception as e:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Error")
            self.expression = ''

root = tk.Tk()  # Create a Tkinter root window
calculator = Calculator(root)  # Create an instance of the Calculator class
root.mainloop()  # Start the GUI event loop
