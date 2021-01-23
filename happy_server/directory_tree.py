import os
# get all filepaths from root node recursivley

# def list_tree(root: str) -> list:
# not working when running the server, why?


def list_tree(root):
    list_of_all_files = os.listdir(root)
    file_list = list()
    for file_name in list_of_all_files:
        abs_path = os.path.join(root, file_name)
        if os.path.isdir(abs_path):
            # when reaching a leaf in the file tree,
            # append absolute file path and recurse
            file_list = file_list + list_tree(abs_path)
        else:
            # remove leading . from absolute file path
            file_list.append(abs_path[1:])

    return file_list
