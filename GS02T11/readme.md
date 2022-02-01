## Task
A folder contains files that are sequentially named as follows, `file1.txt`, `file2.txt`, ..., `fileN.txt` where $N$ is a positive integer. It is of utmost importance that the files are identified by their numbers and not by their names. Design, document and implement an application-layer protocol that allows remote users to perform the following operations:
- Retrieve the content of file $N$.
- Store text in file $N$ and overwrite it if the file already exists.
- Delete file $N$.


## Task

*Optional*. Modify the protocol you obtained in the previous task to consider that files are contained in 26 folders `folderA`,  `folderB`, ..., `folderZ`. It is of utmost importance that the folders are identified by their  letters and not by their names.  Note that file 1 in folder A is not the same as file 1 in folder B. Add a feature that allows remote users to append text to a file.