import axios from '@/libs/api.request'

export const getTableData = () => {
  return axios.request({
    url: 'get_table_data',
    method: 'get'
  })
}

export const getDragList = () => {
  return axios.request({
    url: 'get_drag_list',
    method: 'get'
  })
}

export const errorReq = () => {
  return axios.request({
    url: 'error_url',
    method: 'post'
  })
}

export const saveErrorLogger = info => {
  return axios.request({
    url: 'save_error_logger',
    data: info,
    method: 'post'
  })
}

export const uploadImg = formData => {
  return axios.request({
    url: 'image/upload',
    data: formData
  })
};

/* ---------- API ---------- */

/*—————— 分类 ——————*/
/* 获取所有分类 */
export const getCategorys = formData => {
  return axios.request({
    url: '/categorys/',
  })
};

/*—————— 主题 ——————*/
/* 获取所有主题 */
export const getSubjects = (searchValue, ordering, category, page) => {
  return axios.request({
    url: `/subjects/?type=2&search=${encodeURIComponent(searchValue)}&ordering=${ordering}&category=${category}&page=${page}&page_size=10`,
  })
};

/* 获取某个主题 */
export const getSubject = (id) => {
  return axios.request({
    url: `/subjects/${id}/`,
  })
};

/* 修改主题信息 */
export const saveSubject = (data) => {

  let url = '/subjects/';
  let method = 'post';
  if (data.id) {
    url = `/subjects/${data.id}/`;
    method = `put`;
  }
  return axios.request({
    url: url,
    data: data,
    method: method
  })
};


/*—————— 播放线路 ——————*/

/* 获取主题的所有播放线路 */
export const getlines = (sid) => {
  return axios.request({
    url: `/lines/?subject=${sid}&ordering=order,id`,
  })
};

/* 保存播放列表 */
export const saveLine = (data) => {

  let url = '/lines/';
  let method = 'post';
  if (data.id) {
    url = `/lines/${data.id}/`;
    method = `put`;
  }
  return axios.request({
    url: url + '?type=simple',
    data: data,
    method: method
  })
};

/* 删除播放列表 */
export const delLine = (lineId) => {
  return axios.request({
    url: `/lines/${lineId}/`,
    method: 'delete'
  })
};

/* 修改主题的播放列表顺序 */
export const setlinesSort = (data) => {
  return axios.request({
    url: `/lines/sort/`,
    data: data,
    method: 'put'
  })
};

/*—————— 视频 ——————*/
/* 修改视频顺序 */
export const setVideoSort = (data) => {
  return axios.request({
    url: `/videos/sort/?ordering=order,-add_time`,
    data: data,
    method: 'put'
  })
};

/* 获取视频信息 */
export const getVideo = (id) => {
  return axios.request({
    url: `/videos/${id}/?type=2`,
  })
};

/* 修改视频信息 */
export const saveVideo = (data) => {
  let url = '/videos/';
  let method = 'post';
  if (data.id) {
    url = `/videos/${data.id}/?type=2`;
    method = `put`;
  }

  return axios.request({
    url: url,
    data: data,
    method: method
  })
};

/* 删除视频信息 */
export const delVideo = (videoId) => {
  return axios.request({
    url: `/videos/${videoId}/`,
    method: 'delete'
  })
};


/*—————— 爬虫 ——————*/

/* 修改爬虫信息 */
export const saveSpider = (data) => {
  let url = '/spiders/';
  let method = 'post';
  if (data.id) {
    url = `/spiders/${data.id}/?type=2`;
    method = `patch`;
  }
  return axios.request({
    url: url,
    data: data,
    method: method
  })
};

/* 获取主题的所有爬虫 */
export const getSpiders = (sid, type) => {
  return axios.request({
    url: `/spiders/?owner=${sid}&spider_type=${type}&ordering=order,id`,
  })
};

/* 获取爬虫信息 */
export const getSpider = (id) => {
  return axios.request({
    url: `/spiders/${id}/?type=2`,
  })
};

/* 删除爬虫信息 */
export const delSpider = (id) => {
  return axios.request({
    url: `/spiders/${id}/`,
    method: 'delete'
  })
};

/* 修改主题的爬虫顺序 */
export const setSpiderSort = (data) => {
  return axios.request({
    url: `/spiders/sort/`,
    data: data,
    method: 'patch'
  })
};

/*—————— 视频解析 ——————*/

/* 修改解析信息 */
export const saveVideoParse = (data) => {
  let url = '/parses/';
  let method = 'post';
  if (data.id) {
    url = `/spiders/${data.id}/?type=2`;
    method = `patch`;
  }
  return axios.request({
    url: url,
    data: data,
    method: method
  })
};

/* 获取所有解析接口 */
export const getVideoParses =() => {
  return axios.request({
    url: `/parses/`,
  })
};
