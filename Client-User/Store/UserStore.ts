import { create } from 'zustand'

type Store = {
  user: null
}

const useStore = create<Store>()((set) => ({
  user: null
}));