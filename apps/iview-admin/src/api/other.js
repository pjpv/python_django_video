import axios from '@/libs/api.request'

axios.jsonp = (url) => {
  if (!url) {
    console.error('Axios.JSONP 至少需要一个url参数!')
    return;
  }
  return new Promise((resolve, reject) => {
    window.jsonCallBack = (result) => {
      resolve(result)
    };
    var JSONP = document.createElement("script");
    JSONP.type = "text/javascript";
    JSONP.src = `${url}&callback=jsonCallBack`;
    document.getElementsByTagName("head")[0].appendChild(JSONP);
    setTimeout(() => {
      document.getElementsByTagName("head")[0].removeChild(JSONP)
    }, 500)
  })
};

/* ---------- API ---------- */

/* 获取所有分类 */
export const getDoubanMovie = id => {
  return axios.jsonp(`//api.douban.com/v2/movie/subject/${id}?apikey=0b2bdeda43b5688921839c8ecb20399b`)
};
