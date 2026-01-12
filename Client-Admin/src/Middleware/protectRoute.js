import { NavLink } from "react-router-dom";

const is_auth = () => {
    return localStorage.getItem("auth_token") === "true";
}

export const protectRoute = ({ children }) => {
    if (is_auth()) {
        return children;
    } else {
        <NavLink to="/" />;
    }
}