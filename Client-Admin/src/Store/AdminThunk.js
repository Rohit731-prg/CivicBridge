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
                error: "Error in logging in"
            });
        } catch (error) {
            console.log("Error in login thunk: ", error);
        }
    }
)