import axios from "axios";

const BASE_URL = 'http://localhost:8000/';

export const endpoints  ={
    'categories' : '/categories/'
}

export default axios.create({
    baseURL: BASE_URL
});