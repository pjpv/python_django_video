import axios from './api'

/* 将所有接口统一起来便于维护
 * 如果项目很大可以将 url 独立成文件，接口分成不同的模块
 */


export const getIndexList = () => {
    return axios({url: `/categorys/?ordering=order`, method: 'get'});
};

export const getHeadCategorys = () => {
    return axios({url: `/categorys/?inHead=true&ordering=order`, method: 'get'});
};

export const getCategory = id => {
    if (id) {
        return axios({url: `/categorys/${id}/`, method: 'get'});
    } else {
        return {};
    }
};

export const getSubjects = (cid, page) => {
    if (cid) {
        return axios({url: `/subjects/?category=${cid}&ordering=-pub_date,-update_time&page=${page}`, method: 'get'});
    } else {
        return {};
    }
};
export const getSubject = id => {
    if (id) {
        return axios({url: `/subjects/${id}/`, method: 'get'});
    } else {
        return {};
    }
};
export const searchSubject = (text, category, page) => {
    if (text) {
        return axios({url: `/subjects/?search=${encodeURIComponent(text)}&category=${category}&page=${page}`, method: 'get'});
    } else {
        return {};
    }
};
export const getLines = sid => {
    if (sid) {
        return axios({url: `/lines/?subject=${sid}`, method: 'get'});
    } else {
        return {};
    }
};
export const getVideo = vid => {
    if (vid) {
        return axios({url: `/videos/${vid}/`, method: 'get'});
    } else {
        return {};
    }
};


// 默认全部导出
export default {
    getIndexList,
    getHeadCategorys,
    getCategory,
    getSubjects,
    getSubject,
    getLines,
    getVideo,
    searchSubject,
}