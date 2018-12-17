Tags: git
Status: draft

The idea is storing images for Github readme file on the repo itself. This can be done by using the relative image path of Github ([more info](https://help.github.com/articles/about-readmes/#relative-links-and-image-paths-in-readme-files)). For example: `![Github Logo](/images/logo.png)`

The path in between the `()` is the path of file on the repo itself. Github automatically uses the branch of displayed readme, or in other words, the current branch of the displayed page.

The images can be hidden in another branch but still accessible. To do this, use relative link operand. For example: `../assets/images/logo.png` leads to branch `assets`, directory `images` and then `logo.png` file.

An example of creating another branch for images is as followed (starts with `images` directory at the root of the repo):

```shell
git checkout --orphan assets
git rm -rf .
git add images/
git commit -m "add images for Github readme"
git push origin assets
```

Remember to remove `images` directory on `master` branch:

```shell
git checkout master
git rm -rf images/
```
