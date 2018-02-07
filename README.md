
## 1.建立json文件

    yum install nodejs

    在静态网页文件夹下
    npm install -g hugo-lunr-zh
    会生成一个node_modules文件夹

    cd /Users/tanqianshan/Documents/3.blog/blog-mainroad
    hugo-lunr-zh  -o public/data.json --matter-delims --- --matter-type yaml -d content/math/significance_test -c /math/significance_test/
    -o 未生成的json文件，-d为需要建立json文件的md文件，但这个参数没办法进行递归查找 -contextPath 生成的uri前缀

因为hugo-lunr-zh不具有递归处理的能力，所以需要用python来处理，给每个文件夹生成一个json文件，然后再合并


## 2. 网页版的处理
