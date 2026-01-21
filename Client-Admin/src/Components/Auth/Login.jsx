import { MdEmail } from "react-icons/md";
import { FaLock } from "react-icons/fa6";
import { FaEye, FaEyeSlash } from "react-icons/fa";
import { useState } from "react";

function Login() {
  const [passwordShow, setPasswordShow] = useState(false)
  return (
    <main className="p-20 flex flex-row items-center gap-10 w-full min-h-screen">
      <section className="w-1/2"></section>

      <section className="w-1/2">
        <h1 className="text-2xl font-medium">Welcome Back</h1>
        <p className="text-md text-gray-400">Fill the details for login</p>


        <form action="" className="py-10 w-1/2">
          <label htmlFor="" className="">Email ID</label>
          <div className="flex flex-row mt-3 mb-5 gap-3 items-center outline-none border-b-2 border-black">
              <MdEmail className="text-gray-200" />
              <input type="email" placeholder="Enter Email Address" />
          </div>

          <label htmlFor="" className="">Passwoord</label>
          <div className="flex flex-row mt-3 justify-between items-center outline-none border-b-2 border-black">
              <div className="flex flex-row gap-3">
                  <MdEmail className="text-gray-200" />
                  <input type="password" placeholder="Enter Email Address" />
              </div>
              <button>
                {passwordShow ? <FaEye /> : <FaEyeSlash />}
              </button>
          </div>

          <button className="w-full my-10 py-3 rounded-full bg-blue-600 text-white font-medium">
            SUBMIT
          </button>
        </form>
      </section>
    </main>
  )
}

export default Login