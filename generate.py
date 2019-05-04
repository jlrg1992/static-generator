import os

markdowns = os.listdir('markdown')
print("Markdown files to convert: "+str(len(markdowns)))
os.system('rm -rf html-content/posts/')
os.makedirs('html-content/posts')

for m in markdowns:
    os.system('pandoc markdown/'+m+' -o html-content/posts/'+m[:-8]+'.html')

posts = os.listdir('html-content/posts')
print('Html files converted: '+str(len(posts)))