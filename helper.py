def main():
    root = tkinter.Tk()
    root.geometry("600x400")
    root.resizable(False, False)

    icon = PhotoImage(file="./img/icon_min.png")
    root.iconphoto(False, icon)

    btn = tkinter.Button(text="Cancel")
    btn.bind("<Button-1>", exit)
    canv = tkinter.Canvas(width=600, height=400, bg='lightgray')
    canv.pack()
    btn.pack()


    
    # return root
    root.mainloop()

if __name__ == "__main__":
    with open("main.log", "a") as log:
        try:
            import tkinter
            from tkinter import PhotoImage
            import datetime

            now = datetime.datetime.now()
            
            main()
            log.write("\n[  OK  ] datetime: " + now.strftime("%Y-%m-%d %H:%M:%S") + "  -  file: helper.py")

        except KeyboardInterrupt:
            log.write("\n[  OK  ] datetime: " + now.strftime("%Y-%m-%d %H:%M:%S") + "  -  file: helper.py")
        except ModuleNotFoundError:
            log.write("\n[  FAIL  ] datetime: " + now.strftime("%Y-%m-%d %H:%M:%S" + " Module not found") + "  -  file: helper.py")
        except ImportError:
            log.write("\n[  FAIL  ] datetime: " + now.strftime("%Y-%m-%d %H:%M:%S" + " Import Error") + "  -  file: helper.py")
        except NameError:
            log.write("\n[  FAIL  ] datetime: " + now.strftime("%Y-%m-%d %H:%M:%S" + " Name Error") + "  -  file: helper.py")