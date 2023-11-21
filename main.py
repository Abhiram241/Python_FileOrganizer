import os
import sys
import shutil as shoot
import customtkinter as ctk
import tkinter as tk  # Import tkinter for Frame widget

fol1 = "OneZ"
fol2 = "Utility"
fol3 = "TheGrayMatter"
fol4 = "Take a look here"
wd = os.getcwd()
this_file = "main.py"
s_Folders = [fol1, fol2, fol3, fol4, this_file, 'temp.py']


# remember to uncomment this_file editing it


def ui():
    def frame_home():
        def delete_frame():
            def add_frame():
                def exit_fn():
                    sys.exit(0)

                def transition():
                    root.destroy()
                    ui()

                for widget in root.winfo_children():
                    widget.pack_forget()
                    # Display "Please wait..." for 2 seconds
                    waiter = ctk.CTkLabel(root, text="Please wait...", font=("Arial", 24, "bold"), anchor='center',
                                          text_color='#FFFFFF')
                    waiter.pack(pady=(70, 10))
                    root.update()  # Update the GUI to show the label
                    root.after(2000,
                               lambda: waiter.pack_forget())  # Remove the label after 2000 milliseconds (2 seconds)

                    # Add the "Job done!" label and buttons after a delay
                    root.after(3000)
                frame_exit = tk.Frame(root, background='#202020')
                frame_exit.pack()
                frame_exit.tkraise()
                done_label = ctk.CTkLabel(frame_exit, text="Job done!", font=("Arial", 24, "bold"), anchor='center',
                                          text_color='#FFFFFF')
                done_label.pack(pady=(40, 20))
                cont_b = ctk.CTkButton(frame_exit, text="Main menu", command=transition)
                cont_b.pack(pady=(0, 10))
                exit_b = ctk.CTkButton(frame_exit, text="Finish", command=exit_fn)
                exit_b.pack(pady=(0, 0))

            add_frame()

        def mov(source_folder, folder_d, item, sf1, ext):
            if not os.path.exists(os.path.join(source_folder, sf1)):
                os.makedirs(os.path.join(source_folder, sf1))
            destination_file_path = os.path.join(source_folder, sf1, item)
            n = 0
            counter = 1
            if os.path.exists(destination_file_path):
                if '-copy' in item:
                    n_item = f'{item}-copy{counter + 1}{ext}'
                    os.rename(folder_d, os.path.join(source_folder, n_item))
                else:
                    n_item = f'{item}-copy{counter}{ext}'
                    os.rename(folder_d, os.path.join(source_folder, n_item))
                n = 1
            if n == 0:
                shoot.move(os.path.join(source_folder, item), os.path.join(source_folder, sf1))
            elif n == 1:
                shoot.move(os.path.join(source_folder, n_item), os.path.join(source_folder, sf1))

        def file_type():
            sf1 = 'Python Files'
            sf2 = 'Documents'
            sf3 = 'Excel'
            sf4 = 'Presentation'
            sf5 = 'Images'
            sf6 = 'Videos'
            sf7 = 'Audio'
            sf8 = 'Compressed files'
            sf9 = 'Web development'
            sf10 = 'Folders'
            sf11 = 'Installers'
            sf12 = 'Misc'
            sorts = [sf1, sf2, sf3, sf4, sf5, sf6, sf7, sf8, sf9, sf10, sf11, sf12]

            n = 0
            n_item = '-'
            source_folder = ctk.filedialog.askdirectory()
            file_list = os.listdir(source_folder)
            print(file_list)
            for item in file_list:
                folder_d = os.path.join(source_folder, item)
                if os.path.isdir(folder_d):
                    if item not in sorts:
                        if not os.path.exists(os.path.join(source_folder, sf10)):
                            os.makedirs(os.path.join(source_folder, sf10))
                        destination_file_path = os.path.join(source_folder, sf10, item)
                        counter = 1
                        if os.path.exists(destination_file_path):
                            if '-copy' in item:
                                n_item = f'{item}-copy{counter + 1}'
                                os.rename(folder_d, os.path.join(source_folder, n_item))
                            else:
                                n_item = f'{item}-copy{counter}'
                                os.rename(folder_d, os.path.join(source_folder, n_item))
                            n = 1
                        if n == 0:
                            shoot.move(os.path.join(source_folder, item), os.path.join(source_folder, "Folders"))
                        elif n == 1:
                            shoot.move(os.path.join(source_folder, n_item), os.path.join(source_folder, "Folders"))

                if item.endswith('.py'):
                    mov(source_folder, folder_d, item, sf1, '.py')
                elif item.endswith('.txt'):
                    mov(source_folder, folder_d, item, sf2, '.txt')
                elif item.endswith('.docx'):
                    mov(source_folder, folder_d, item, sf2, '.docx')
                elif item.endswith('.csv'):
                    mov(source_folder, folder_d, item, sf2, '.csv')
                elif item.endswith('.epub'):
                    mov(source_folder, folder_d, item, sf2, '.epub')
                elif item.endswith('.pdf'):
                    mov(source_folder, folder_d, item, sf2, '.pdf')
                elif item.endswith('.c'):
                    mov(source_folder, folder_d, item, sf12, '.c')
                elif item.endswith('.xlsx'):
                    mov(source_folder, folder_d, item, sf3, '.xlsx')
                elif item.endswith('.pptx'):
                    mov(source_folder, folder_d, item, sf4, '.pptx')
                elif item.endswith('.jpeg'):
                    mov(source_folder, folder_d, item, sf5, '.jpeg')
                elif item.endswith('.png'):
                    mov(source_folder, folder_d, item, sf5, '.png')
                elif item.endswith('.gif'):
                    mov(source_folder, folder_d, item, sf5, '.gif')
                elif item.endswith('.jpg'):
                    mov(source_folder, folder_d, item, sf5, '.jpg')
                elif item.endswith('.webp'):
                    mov(source_folder, folder_d, item, sf5, '.webp')
                elif item.endswith('.svg'):
                    mov(source_folder, folder_d, item, sf5, '.svg')
                elif item.endswith('.mov') or item.endswith('.mp4') or item.endswith('.mkv') or item.endswith('.avi'):
                    mov(source_folder, folder_d, item, sf6, item[-4:])
                elif item.endswith('.mp3') or item.endswith('.wav'):
                    mov(source_folder, folder_d, item, sf7, item[-4:])
                elif item.endswith('.zip') or item.endswith('.rar'):
                    mov(source_folder, folder_d, item, sf8, item[-4:])
                elif item.endswith('.7z'):
                    mov(source_folder, folder_d, item, sf8, item[-3:])
                elif item.endswith('.html'):
                    mov(source_folder, folder_d, item, sf9, item[-5:])
                elif item.endswith('.json'):
                    mov(source_folder, folder_d, item, sf12, item[-5:])
                elif item.endswith('.css'):
                    mov(source_folder, folder_d, item, sf9, item[-4:])
                elif item.endswith('.js'):
                    mov(source_folder, folder_d, item, sf9, item[-3:])
                elif item.endswith('.exe') or item.endswith('.msi'):
                    mov(source_folder, folder_d, item, sf11, item[-4:])
                else:
                    if os.path.exists(folder_d):
                        if item not in sorts:
                            if not os.path.exists(os.path.join(source_folder, sf12)):
                                os.makedirs(os.path.join(source_folder, sf12))
                            destination_file_path = os.path.join(source_folder, sf12, item)
                            counter = 1
                            if os.path.exists(destination_file_path):
                                if '-copy' in item:
                                    n_item = f'{item}-copy{counter + 1}'
                                    os.rename(folder_d, os.path.join(source_folder, n_item))
                                else:
                                    n_item = f'{item}-copy{counter}'
                                    os.rename(folder_d, os.path.join(source_folder, n_item))
                                n = 1
                            if n == 0:
                                shoot.move(os.path.join(source_folder, item), os.path.join(source_folder, sf12))
                            elif n == 1:
                                shoot.move(os.path.join(source_folder, n_item), os.path.join(source_folder, sf12))
                        else:
                            print("here")
                            extension=item.split('.')
                            print(extension)
            delete_frame()

        def next_b():
            if check_state.get():
                creation()
                main()
                print("under progress")
            else:
                folder_path = ctk.filedialog.askdirectory()

                # wd1 = folder_path.replace("/", '\\')
                # print("I have " + str(wd1))
                creation1(folder_path)
                main1(folder_path)
            for widget in root.winfo_children():
                widget.pack_forget()
            delete_frame()
            # done_label = ctk.CTkLabel(root, text="Job done!", font=("Arial", 24, "bold"), anchor='center')
            # done_label.pack(pady=(60, 20))
            # cont_b = ctk.CTkButton(frame_e, text="Main menu", command=ui)
            # cont_b.pack(pady=(0,0))
            # exit_b = ctk.CTkButton(root, text="Finish", command=quit)
            # exit_b.pack(pady=(0, 0))

        def the_manual():
            def transition():
                root.destroy()
                ui()

            guide = ('Organize folder: When you click this button without marking the checkbox,the files in current '
                     'folder will be organized inside OneZ,you can check the box to organize other folders.\n')
            for widget in root.winfo_children():
                widget.pack_forget()
            frame_m = tk.Frame(root, background='#202020')
            frame_m.pack()
            manual_h = ctk.CTkLabel(frame_m, text="Guide", font=("Arial", 24, "bold"), text_color='#FFFFFF')
            manual_h.pack(pady=(20, 0))
            manual = ctk.CTkLabel(frame_m, text=guide, font=("Arial", 15), text_color='#FFFFFF',
                                  anchor='w', wraplength=350)
            manual.pack(pady=(10, 3))
            back_b = ctk.CTkButton(frame_m, text="Main menu", command=transition)
            back_b.pack(pady=(0, 10))

        frame_h = tk.Frame(root, background='#202020')  # background='#352F44'
        frame_h.pack()  # you are creating a new frame here
        frame_h.tkraise()
        heading = ctk.CTkLabel(frame_h, text="Welcome to File Organizer", font=("Arial", 24, "bold"),
                               text_color='#FFFFFF')
        heading.pack(padx=10, pady=10, anchor='center')  # Use 'nw' anchor to position in the top-left corner
        check_state = ctk.BooleanVar()
        frame_o = tk.Frame(frame_h, background='#202020')
        frame_o.pack(pady=(15, 10))

        # Create a button to trigger the folder dialog
        open_folder_button = ctk.CTkButton(frame_o, text="Organize folder", command=next_b)
        open_folder_button.pack(padx=0, side='left')
        checkbox = ctk.CTkCheckBox(frame_o, text="This folder", variable=check_state, text_color='#FFFFFF')
        checkbox.pack(side='left', padx=20)
        frame_s = tk.Frame(frame_h, background='#202020')
        frame_s.pack(pady=(1, 10))
        sort_b = ctk.CTkButton(frame_s, text="Sort Files", command=file_type)
        sort_b.pack(side='left')
        label = ctk.CTkLabel(frame_s, text="Sort files by type", font=("Arial", 13), text_color='#FFFFFF')
        label.pack(side='left', padx=(20, 20))
        sort_b = ctk.CTkButton(frame_h, text="Know your tool", command=the_manual)
        sort_b.pack(pady=(7, 10))

    root = tk.Tk()
    root.geometry("400x200")
    root.title("Folder organizer")
    root.configure(bg="#202020")
    root.resizable(False, False)
    frame_home()

    root.mainloop()


def readme(folder):
    path = os.path.join(wd, folder, 'readme.txt')
    with open(path, 'w') as f:
        if folder == fol3:
            f.write(f"{folder} should include all the files and folders for which a decision regarding inclusion has "
                    f"not"
                    f"been determined.")
        elif folder == fol1:
            f.write(f"{folder} should consist of files and folders that meet your temporary needs, including items "
                    f"like installers and other non-permanent files which can be left behind when you reset your "
                    f"os.\n{'By Default all the files/folders are shifted here'.upper()} ")
        elif folder == fol2:
            f.write(f"{folder} should consist all the utilities you might require")
        elif folder == fol4:
            f.write(f"{folder} will consist all the folders that were there in downloads folder")


def readme1(folder, wd1):
    path = os.path.join(wd1, folder, 'readme.txt')
    with open(path, 'w') as f:
        if folder == fol3:
            f.write(f"{folder} should include all the files and folders for which a decision regarding inclusion has "
                    f"not"
                    f"been determined.")
        elif folder == fol1:
            f.write(f"{folder} should consist of files and folders that meet your temporary needs, including items "
                    f"like installers and other non-permanent files which can be left behind when you reset your "
                    f"os.\n{'By Default all the files/folders are shifted here'.upper()} ")
        elif folder == fol2:
            f.write(f"{folder} should consist all the utilities you might require")
        elif folder == fol4:
            f.write(f"{folder} will consist all the folders that were there in downloads folder")


def creation():
    os.makedirs(fol1, exist_ok=True)
    readme(fol1)
    os.makedirs(fol2, exist_ok=True)
    readme(fol2)
    os.makedirs(fol3, exist_ok=True)
    readme(fol3)
    os.makedirs(fol4, exist_ok=True)
    readme(fol4)


def creation1(wd1):
    os.makedirs(os.path.join(wd1, fol1), exist_ok=True)
    readme1(fol1, wd1)
    os.makedirs(os.path.join(wd1, fol2), exist_ok=True)
    readme1(fol2, wd1)
    os.makedirs(os.path.join(wd1, fol3), exist_ok=True)
    readme1(fol3, wd1)
    os.makedirs(os.path.join(wd1, fol4), exist_ok=True)
    readme1(fol4, wd1)


def main():
    print("i have " + str(wd))
    print("Your current working directory is " + str(wd))
    file_list = os.listdir(wd)

    for i in file_list:
        if i == "readme.txt":
            print("Skipped readme file to prevent conflict")
            continue
        if not os.path.isdir(i):
            if i not in s_Folders:
                shoot.move(f"{wd}\\{i}", os.path.join(wd, "OneZ"))
                print("Moving the file " + str(i))
        else:
            if i not in (os.listdir(fol4)):
                if i not in s_Folders:
                    shoot.move(f"{wd}\{i}", os.path.join(wd, fol4))
                    print(i)
            else:
                print("Conflict detected")


def main1(wd1):
    print("Your current working directory is " + str(wd1))
    file_list = os.listdir(wd1)

    for i in file_list:
        if i == "readme.txt":
            continue
        if not os.path.isdir(i):
            if i not in s_Folders:
                shoot.move(os.path.join(wd1, i), os.path.join(wd1, fol1))
                print("Moving the file " + str(i))
        else:
            if i not in (os.listdir(fol4)):
                if i not in s_Folders:
                    shoot.move(os.path.join(wd1, i), os.path.join(wd1, fol4))
                    print(i)
            else:
                print("Conflict detected")


if __name__ == '__main__':
    ui()
