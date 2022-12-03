import os
print(os.getcwd())

my_dir = "C:\Malini\Precision\codepractice\Training"

# Change Directory to the specified name in my_dir
os.chdir(my_dir)

#check if Current Directory is the one specified in variables "my_dir"
print(os.getcwd())

print(os.listdir(my_dir))
samplefile_dir="C:\Malini\Precision\codepractice\Training"
os.mkdir(samplefile_dir)

print(os.listdir(my_dir))