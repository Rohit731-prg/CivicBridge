import { Route, BrowserRouter as Router, Routes } from "react-router-dom"
import Login from "./Components/Auth/Login"
import Error from "./Components/Error"
import AdminMenege from "./Components/Core/AdminMenege"

function App() {
  return (
    <Router>
      <Routes>
        <Route path="*" element={<Error />} />
        <Route path="/" element={<Login />} />
        {/* <Route path="/admin" element={<protectRoute><AdminMenege /></protectRoute>} /> */}
        <Route path="/admin" element={<AdminMenege />} />
      </Routes>
    </Router>
  )
}

export default App