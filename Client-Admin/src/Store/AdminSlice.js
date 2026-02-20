import { createSlice } from "@reduxjs/toolkit";
import { loginThunk, registerAdminThunk } from "./AdminThunk";

const initialState = {
    loading: false,
    admin: null,
    employees: null
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

            .addCase(registerAdminThunk.pending, (state) => {
                state.loading = true;
            })
            .addCase(registerAdminThunk.fulfilled, (state, action) => {
                state.loading = false;
                state.employees = action.payload;
            })
            .addCase(registerAdminThunk.rejected, (state) => {
                state.loading = false;
            });
    }
})