import React from 'react'

function Error() {
  return (
    <div className='min-h-screen w-full flex flex-col relative items-center justify-center bg-black text-white'>
        <h1 className='text-[250px] font-bold'>404</h1>
        <p className='text-[75px] absolute top-[55%]'>Page not found</p>

        <button 
        onClick={() => window.history.back()}
        className='mt-10 px-6 py-3 bg-white text-black rounded-md font-medium hover:bg-gray-200 transition-colors'>
            Back Home
        </button>
    </div>
  )
}

export default Error