## 约定

1.  所有请求都走HTPS，并且使用POST方式


2.  HTTPS 服务器开启了强制客户端认证，需要客户端把证书文件打包在应用内，才可以访问到服务器.

    浏览器可以导入自制证书，就可以方便的debug


3.  每一个app都会约定一个app id

    后台会配置此app id 所包含的分类ID，以及推荐ID


4.  客户端每个请求都需要在 http header 中添加两个字段:

    X-WALLPAPER-DEVICE: <String>    设备唯一ID

    X-WALLPAPER-APPID: <Int>        APP ID


5.  错误代码放在返回的http status code中. 见下面的错误码
    


## 请求顺序
1.  应用打开后， 发送第一个请求 `/start/`， 服务器用来来统计数据
2.  后面就是各种分类，图片请求.


### `/start/`

请求数据: 无

返回:

    {
        'categories': [
                    {'id': <Int>, 'name': <String>, 'url': <String>},
                    {'id': <Int>, 'name': <String>, 'url': <String>},
                    ...
                ],

        'recommend': <Int>,
    }

`categories`: 这个app的分类列表.

*   `id`: 分类ID
*   `name`: 分类名字
*   `url`: 分类图片 （取此分类的最新一张图片）

`recommend`: 推荐分类ID


### `/category/?id=<Int>&mode=<Int>&page=<Int>&limit=<Int>`

获取某一分类下的图片

*   `id`: 分类ID
*   `mode`: 模式， 1 - 最新； 2 - 最热
*   `page`: 页面， 可以省略，默认1
*   `limit`： 每页数据量， 可以省略，默认60

返回:

    [
        {'id': <String>, 'url': <String>, 'downloads': <Int>},
        {'id': <String>, 'url': <String>, 'downloads': <Int>},
        ...
    ]

返回列表，如果空，表示当前page没有数据

*   `id`: 图片ID
*   `url`: 图片URL
*   `downloads`: 下载量（hot的依据）


### `/download/?id=<String>`

下载图片 （设置壁纸）

*   `id`: 图片ID 

返回： 空



## 错误码

status code | 含义              | 可能的原因
------------|-------------------|----------------
403         | 非法的APP ID      | 此APP ID没有在服务器后台配置
404         | 找不到分类        | 没有此分类，或者此app不包含此分类


