import axios, { AxiosInstance, AxiosRequestConfig } from "axios";

export default class AuthAPIService {

    constructor() {
        this.axiosInstance = axios.create({
            baseURL: `${import.meta.env.VITE_API_URL}`
        });
    }

    async axiosCall(config) {
        try {
            const { data } = await this.axiosInstance.request(config);
            return data;
        } catch (error) {
            return error;
        } 
    }

    async login(email) {
        return this.axiosCall({ method: "get", url: "/login"});
    }

    async logout() {
        return this.axiosCall({ method: "get", url: "/logout"});
    }

    async ping() {
        return this.axiosCall({ method: "get", url: "/ping"});
    }
}

export const authAPI = new AuthAPIService();