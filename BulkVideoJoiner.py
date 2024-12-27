import os
import random
import subprocess

folder_path = r'C:\Users\Administrator\Desktop\Videos'
mp4_files = [f for f in os.listdir(folder_path) if f.endswith('.mp4')]
iteration = 6

if len(mp4_files) >= 3:
    for i in range(iteration):
        selected_files = random.sample(mp4_files, 3)
        list_file_path = os.path.join(folder_path, 'list.txt')

        with open(list_file_path, 'w') as list_file:
            list_file.writelines(f'file {f}\n' for f in selected_files)

        output_file = f'output_{i + 1}.mp4'
        bat_file_path = os.path.join(folder_path, 'merge_videos.bat')

        with open(bat_file_path, 'w') as bat_file:
            bat_file.write(f'ffmpeg -f concat -safe 0 -i list.txt -c copy {output_file} -loglevel error\n')

        subprocess.run([bat_file_path], shell=True)
        print(f'Merge {i + 1}/{iteration} complete: {output_file}')
else:
    print("Not enough mp4 files in the folder!")
