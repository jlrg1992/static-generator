# static-generator
The static site generator that I built to work for me.
I've looked over some of them, but I think they are simply to much for what I need, so I built this little thing. It is not intended to work for everybody.

It is a static site generator using markdown files to generate simple posts. Don't think. It is not made to be a very clean code, but to work.
The code is kind of self explanatory, so there's not much you need to know.

Happy coding!

## Before starting

You'll need to install *pandoc* for it to work. Make sure to create a site directory and a markdown-blog directory.

## About de markdown files

They are supposed to be stored at the markdown-blog directory
The mardown files need some metadata for it to work. It has the following structure:
```
	---
	title: Some title
	subtitle: A little thing here...
	date: Whichever format you want
	---
```

It has to be at the very begining of the markdown file.

If you want to make use of your own template, make sure to use the same names. To use the metadata of each markdown, you'll have to write as:

```
momotitlemomo
momosubtitlemomo
momodatemomo
```

Check out the scripts before using it.

The template I use was made by BlackrockDigital. You can find the original repo at [startbootstrap-clean-blog](https://github.com/BlackrockDigital/startbootstrap-clean-blog)
Make sure to add your javascript and css files in the site directory. If you want to have it as my blog clone this repository and inside of the site directory clone my [blog repo](https://github.com/jlrg1992/blog.git). That way you can have it as a github pages.

Happy coding!!!
