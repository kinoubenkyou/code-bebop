Tags: bash, git, github

Images stored on Github repo can be accessed from the rendered readme. This is convenient, but be aware of the repo size limit of Github. The images can be stored on a dedicated branch, which might help to avoid dangling image files in git history when they are not needed anymore. The idea is deleting the old branch and then creating a brand new one.

This example is writen based on:

- Git 2.17.1

Create an empty branch, named "assets" for example:

```bash
git checkout --orphan assets
```

Remove all files in working tree and index (this means losing your current work if you haven't commit them to other branches):

```bash
git rm -rf .
```

Create a diretory for images and copy them into it:

```bash
mkdir images
cp /path/of/the/image.png ./images
```

Commit and push the branch to Github:

```bash
git add -A
git commit -m "add image"
git push origin assets
```

Switch to the branch you want its readme to render the file, probably branch master:

```bash
git checkout master
```

Add the image with file path as relative link in readme:

```markdown
![](../assets/images/image.png)
```

Commit and push the new readme to Github:

```bash
git add -A
git commit -m "add image to readme"
git push origin master
```
