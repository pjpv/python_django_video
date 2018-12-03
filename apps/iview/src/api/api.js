import axios from 'axios';

// let localhost = 'http://127.0.0.1:8000/api';
let localhost = 'http://192.168.0.88:8000/api';
let remotehost = 'http://127.0.0.1:8000';
let isDev = true;
let host = isDev ? localhost : remotehost;

export const getIndexList = params => {
    return axios.get(`${host}/categorys/?ordering=order`);
};

export const getHeadCategorys = params => {
    return axios.get(`${host}/categorys/?inHead=true&ordering=order`);
};

export const getCategory = id => {
    if (id) {
        return axios.get(`${host}/categorys/${id}`);
    } else {
        return {};
    }
};

export const getSubjects = (cid, page) => {
    if (cid) {
        return axios.get(`${host}/subjects/?&category=${cid}&ordering=-update_time&page=${page}`);
    } else {
        return {};
    }
};
