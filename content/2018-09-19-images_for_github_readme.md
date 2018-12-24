Tags: bash, github

Image for Github readme can be stored right on the repo itself. This can be done through relative link as the file path. For example, link `/images/logo.png` points to image "logo.png" on directory "images" of the repo.

Images can even be accessed across branches with relative link operand. This allows hiding images in a dedicated branch and using the same images for readme files on all branches. For instance, link `../assets/images/logo.png` accesses the images from branch "assets".

To create a dedicated branch for images, named "assets" for example:

```bash
git checkout --orphan assets
```

Remember to remove everything from the branch before adding images:

```bash
git rm -rf
```
