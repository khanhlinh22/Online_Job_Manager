import axios from "axios";

const BASE_URL = 'https://linhdiep.pythonanywhere.com/';

export const endpoints  ={
    'categories' : '/categories/',
    'recruitments': '/recruitments/'
}

export default axios.create({
    baseURL: BASE_URL
});