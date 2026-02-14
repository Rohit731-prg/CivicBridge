import { createSlice } from "@reduxjs/toolkit";
import { loginThunk } from "./AdminThunk";

const initialState = {
    loading: false,
    admin: null
};

export const AdminSlice = createSlice({
    name: "admin",
    initialState,
    reducers: {},
    extraReducers: (builder) => {
        builder
            .addCase(loginThunk.pending, (state) => {
                state.loading = true;
            })
            .addCase(loginThunk.fulfilled, (state, action) => {
                state.loading = false;
                state.admin = action.payload;
            })
            .addCase(loginThunk.rejected, (state) => {
                state.loading = false;
                state.admin = null;
            })
    }
})