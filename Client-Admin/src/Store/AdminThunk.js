import { createAsyncThunk } from "@reduxjs/toolkit";
import { axiosInstance } from "../Utils/axios";
import toast from "react-hot-toast";


export const loginThunk = createAsyncThunk(
    "admin/login",
    async (data, { rejectWithValue }) => {
        try {
            const res = axiosInstance.post("/admin/login", data);
            toast.promise(res, {
                loading: "Logging in...",
                success: (res) => res.data.message,
                error: (err) => err.response?.data?.message || "Error in logging in"
            });
        } catch (error) {
            console.log("Error in login thunk: ", error);
        }
    }
);

export const registerAdminThunk = createAsyncThunk(
    "admin/register",
    async (data, { rejectWithValue }) => {
        try {
            const res = axiosInstance.post("/admin/register", data);
            toast.promise(res, {
                loading: "Registering admin...",
                success: (res) => res.data.message,
                error: (err) => err.response?.data?.message || "Error in registering admin"
            });
        } catch (error) {
            console.log("Error in register admin thunk: ", error);
        }
    }
)