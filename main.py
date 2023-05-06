# This is a sample Python script.
from app.cerc import Cerc
from app.dreptunghi import Dreptunghi


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
    dreptunghi = Dreptunghi(10, 5, "galben")
    dreptunghi.descrie()
    print(f'Aria dreptunghiului este: {dreptunghi.aria()}.')
    print(f'Perimetrul dreptunghiului este: {dreptunghi.perimetrul()}.')
    dreptunghi.schimba_culoarea("verde")
    print(f'Dreptunghiul are acum culoarea: {dreptunghi.culoare}.')

    cerc = Cerc(2, "albastra")
    cerc.descrie_cerc()
    print(f"Aria cercului cu raza implicita este {cerc.aria()}.")
    print(f"Diametrul cercului este {cerc.diametru()}.")
    print(f"Lungimea cercului cu raza 1 este: {cerc.circumferinta(1)}.")