import { authService } from "../services/auth.service";

function setJWTTokenHeader(token) {
    authService.defaults.headers.common['Authorization'] = `Bearer ${token}`;
}

export { setJWTTokenHeader }