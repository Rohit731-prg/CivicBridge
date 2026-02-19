import React from 'react'
import Sidebar from '../Auth/Sidebar'

function AdminMenege() {
    const handelSubmit = (e) => {
        e.preventDefault();
    }

  return (
    <div className='flex flex-row w-full min-h-screen'>
        <Sidebar/>

        <aside className='flex flex-row gap-10'>
            <section className='w-1/2'>
                <form onSubmit={handelSubmit}>
                    
                </form>
            </section>
            <section></section>
        </aside>
    </div>
  )
}

export default AdminMenege