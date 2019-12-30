

def test1():
    # test1 is above initial Dev Eq threshold,
    # has no modification after first commit,
    # and has in-degree of 1
    # but it lives shorter than 365 days
    if os.name != "nt":
        shutil.rmtree(top)
        return

    for root, dirs, files in os.walk(top, topdown=False):
        for name in files:
            filename = os.path.join(root, name)
            os.chmod(filename, stat.S_IWUSR)
            os.remove(filename)
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    os.rmdir(top)


def test2():
    # test 2 lives longer than 365 days,
    # has no modification after first commit,
    # and has an in-degree of 1
    # but its initial Dev Eq is smaller than 25
    pass


def test3():
    # test 3 is above initial Dev Eq threshold,
    # lives longer than a year,
    # and has an in-degree o 1
    # but is heavily modified afterwards
    for item in os.listdir(dir_path):
        # Do not delete the .git directory
        if item == ".git":
            continue
        path = os.path.join(dir_path, item)
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)


def test4():
    # test 4 is above initial Dev Eq threshold,
    # lives longer than a year,
    # and is never modified after its first commit,
    # but has no in-degree and out-degree
    remove_all_except_git(dest_repo_path)
    copy_tree_except_git(src_repo_path, dest_repo_path)
    dest_repo.git.add("*")
    # set committer to the same as author
    dest_repo.git.config("user.name", author_name)
    dest_repo.git.config("user.email", author_email)
    # make the commit
    dest_repo.git.commit("-m {}".format(commit_msg),
                         "--author='{} <{}>'".format(author_name, author_email),
                         "--date={}".format(authored_date))
    sha = dest_repo.git.rev_parse("HEAD")
    return sha


test1()
test2()
test3()
