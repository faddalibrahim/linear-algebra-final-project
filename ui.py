# Import the needed libraries.
from calculator import calculate

from tkinter import *
import customtkinter

import matplotlib.pyplot as plt

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")


class GramSchmidt(customtkinter.CTk):
    """
    The GUI class.
    """

    def __init__(self):
        self.result = None
        """
        The constructor. This is where the tkinter
        frame is built and all the components are a
        added.
        """

        super().__init__()

        self.title("Gram-Schmidt Calculator")
        self.geometry(f"{600}x{600}")

        # Add a "spacer" label.
        Label(self, text="", bg="lightgray").grid(row=4, column=0, sticky=N)

        self.resultLabel = Label(self, text="", bg="lightgray")
        self.resultLabel.grid(row=3, column=0, columnspan=2, sticky=N)

        self.rowEntryBox = customtkinter.CTkEntry(master=self,
                                                  text_font=(
                                                      "Product Sans", 10),
                                                  placeholder_text="Number of Entries",
                                                  width=130,
                                                  height=40,
                                                  border_width=0,
                                                  corner_radius=4,
                                                  )

        self.rowEntryBox.grid(row=1, column=1, padx=10, pady=10)

        self.columnEntryBox = customtkinter.CTkEntry(master=self,
                                                     text_font=(
                                                         "Product Sans", 10),
                                                     placeholder_text="Number of Vectors",
                                                     width=130,
                                                     height=40,
                                                     border_width=0,
                                                     corner_radius=4)

        self.columnEntryBox.grid(row=1, column=2)

        calculateButton = customtkinter.CTkButton(master=self,
                                                  text_font=(
                                                      "Product Sans", 10),
                                                  width=120,
                                                  height=40,
                                                  border_width=0,
                                                  corner_radius=4,
                                                  text="Calculate",
                                                  command=lambda: self.calculate()).grid(row=1, column=4, sticky=W, pady=10, padx=10)

        generateVectorsButton = customtkinter.CTkButton(master=self,
                                                        text_font=(
                                                            "Product Sans", 10),
                                                        width=120,
                                                        height=40,
                                                        border_width=0,
                                                        corner_radius=4,
                                                        text="Generate Vectors",
                                                        command=lambda: self.generateVectors()).grid(row=1, column=3, sticky=W, pady=10, padx=10)

        # Set the default dimensions.
        self.rowsNeeded = 0
        self.columnsNeeded = 0

        # The entry boxes for the vectors.
        self.entries = []
        self.labels = []
        self.rowPositions = []
        self.columnPoisitions = []

        self.grid()

    def generateVectors(self):
        """
        Reads the dimensions from their respective
        entry boxes. Then, it uses it to generate 
        empty vectors.
        """

        # First, remove the current entries.
        self.clear()

        # Where should we start displaying the entries?
        startRow = 2
        startColumn = 0

        # Grab the dimensions to make.
        self.rowsNeeded = self.rowEntryBox.get()
        self.columnsNeeded = self.columnEntryBox.get()

        # Did the user enter an integer? If not, don't do anything.
        try:
            self.rowsNeeded = int(self.rowsNeeded)
            self.columnsNeeded = int(self.columnsNeeded)
        except ValueError:
            return

        # Add titles.
        for i in range(self.columnsNeeded):
            temp = customtkinter.CTkLabel(master=self,
                                          text="x{}".format(str(i+1)),
                                          text_color=("black"),
                                          text_font=("Product Sans", 12),
                                          width=10,
                                          height=10,
                                          fg_color=("lightgreen"),
                                          corner_radius=1.5)
            temp.grid(row=startRow, column=startColumn+i, sticky=N, padx=4)
            self.labels.append(temp)

        # Increment it since we just added vector names.
        startRow += 1

        # Clear the self.entries list and the position lists.
        self.entries = []

        # Add the entries.
        for i in range(self.rowsNeeded):
            for j in range(self.columnsNeeded):
                e = customtkinter.CTkEntry(
                    master=self, width=10, corner_radius=2)
                e.grid(row=startRow + i, column=startColumn + j, padx=4)
                self.entries.append([e, j])

    def calculate(self):
        """
        Grab the input entries and put them in
        a list that the calculator script can 
        use.
        """

        # Create an empty list.
        vectors = []

        # Clear the result label alone.
        self.resultLabel.configure(text="", bg="lightgray")

        # Do nothing if the size hasn't been set.
        if self.columnsNeeded == 0 or self.rowsNeeded == 0:
            return

        # Prepare the vectors.
        for i in range(self.columnsNeeded):
            vectors.append([])

        # Grab all the entries. If one doesn't exist or one has the wrong type, do nothing.
        try:
            for entry in self.entries:
                vector = entry[1]
                if "" == entry[0].get():
                    return
                vectors[vector].append(int(entry[0].get()))

        except(TypeError, ValueError):
            return

        # Calculate the resulting basis.
        result = calculate(vectors)

        # Output the result to the GUI.
        # self.plot(result)
        self.displayResult(result)
        self.result = result

    def displayResult(self, result):
        """
        Display the result in the GUI.
        This is nothing fancy.
        """

        # Float all the results for uniformity.
        for i in range(len(result)):
            for j in range(len(result[i])):
                result[i][j] = float(result[i][j])

        # Create the result string to display.
        s = ""
        c = 1
        for res in result:
            s = s + "V" + str(c) + " = {}".format(res) + "\n"
            c += 1

        # Display the result.
        # self.resultLabel = Label(self, text=s[:-1], font=4, bg="lightgreen")
        # self.resultLabel.grid(row=5, column=0, columnspan=2, sticky=N)

        self.resultLabel = customtkinter.CTkLabel(master=self,
                                                  text=s[:-1],
                                                  width=200,
                                                  height=120,
                                                  bg_color=("#333"),
                                                  corner_radius=8)
        self.resultLabel.grid(row=7, column=1, pady=20)

    def clear(self):
        """
        Clears all the entries in the GUI.
        """

        # Clear the entries.
        for entry in self.entries:
            entry[0].grid_forget()

        # Erase the vector labels.
        for label in self.labels:
            label.grid_forget()

        # Erase the result label.
        self.resultLabel.configure(text="", bg="lightgray")

        # Empty the entries list and the labels list.
        self.entries = []
        self.labels = []

    def plot(self, vectors):
        print(vectors)
        fig = plt.figure()
        ax = plt.axes(projection='3d')

        xs = []
        ys = []
        zs = []

        for i in range(len(vectors)):
            vector = vectors[i]

            for j in range(len(vector)):
                if j == 0:
                    xs.append(vector[j])
                if j == 1:
                    ys.append(vector[j])
                if j == 2:
                    zs.append(vector[j])

        ax.set_xlim([min(xs)-1, max(xs)+1])
        ax.set_ylim([min(ys)-1, max(ys)+1])
        ax.set_zlim([min(zs)-1, max(zs)+1])

        ax.quiver(0, 0, 0, vectors[0][0], vectors[0]
                  [1], vectors[0][2], color='r')
        ax.quiver(0, 0, 0, vectors[1][0], vectors[1]
                  [1], vectors[1][2], color='b')
        ax.quiver(0, 0, 0, vectors[2][0], vectors[2]
                  [1], vectors[2][2], color='g')

        plt.show()
