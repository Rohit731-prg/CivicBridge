import React, { useState } from 'react'
import Sidebar from '../Auth/Sidebar'
import { registerAdminThunk } from '../../Store/AdminThunk';
import { stateDtails } from '../../Utils/StateDetails';

function AdminMenege() {
    const [districts, setDistricts] = useState(null);
    const [municipalities, setMunicipalities] = useState(null);
    const [wards, setWards] = useState(null);
    const [jurisdiction, setJurisdiction] = useState({
        state: "",
        district: "",
        municipality: "",
        ward_nos: [],
    });
    const [adminDetails, setAdminDetails] = useState({
        name: '',
        employee_ID: '',
        authority_type: '',
        phone: '',
        email: '',
        password: '',
        jurisdiction: jurisdiction
    });

    const handelSubmit = async (e) => {
        e.preventDefault();
        registerAdminThunk(adminDetails);
    }

  return (
    <div className='flex flex-row w-full min-h-screen'>
        <Sidebar/>

        <aside className='flex flex-row gap-10'>
            <section className='w-1/2'>
                <form onSubmit={handelSubmit}>
                    <label htmlFor="name">Name : </label>
                    <input type="text" required value={adminDetails.name}
                    placeholder='Enter Employee Name'
                    onChange={(e) => setAdminDetails({ ...adminDetails, name: e.target.value })} />

                    <label htmlFor="employee_ID">Employee ID : </label>
                    <input type="text" required value={adminDetails.employee_ID}
                    placeholder='Enter Employee ID'
                    onChange={(e) => setAdminDetails({ ...adminDetails, employee_ID: e.target.value })} />
                    
                    <label htmlFor="authority_type">Authority Type : </label>
                    <select required value={adminDetails.authority_type}
                    onChange={(e) => setAdminDetails({ ...adminDetails, authority_type: e.target.value })}>
                        <option value="">Select Authority Type</option>
                        <option value="State">State</option>
                        <option value="District">District</option>
                        <option value="Municipality">Municipality</option>
                    </select>

                    <label htmlFor="phone">Phone : </label>
                    <input type="text" required value={adminDetails.phone}
                    placeholder='Enter Phone Number'
                    onChange={(e) => setAdminDetails({ ...adminDetails, phone: e.target.value })} />

                    <label htmlFor="email">Email : </label>
                    <input type="email" required value={adminDetails.email}
                    placeholder='Enter Email'
                    onChange={(e) => setAdminDetails({ ...adminDetails, email: e.target.value })} />
                    
                    <label htmlFor="password">Password : </label>
                    <input type="password" required value={adminDetails.password}
                    placeholder='Enter Password'
                    onChange={(e) => setAdminDetails({ ...adminDetails, password: e.target.value })} />

                    <p>Address Section</p>

                    <label htmlFor="state">State : </label>
                    <select required value={adminDetails.jurisdiction.state}
                    onChange={(e) => {
                        const selectedState = e.target.value;
                        setAdminDetails({ ...adminDetails, jurisdiction: { ...adminDetails.jurisdiction, state: selectedState } });
                        const stateInfo = stateDtails.find(state => state.state === selectedState);
                        if (stateInfo) {
                            setDistricts(stateInfo.districts);
                            setMunicipalities(null);
                            setWards(null);
                        }
                    }}>
                        <option value="">Select State</option>
                        {stateDtails.map((state, index) => (
                            <option key={index} value={state.state}>{state.state}</option>
                        ))}
                    </select>

                    <label htmlFor="district">District : </label>
                    {districts ? (
                        <select>
                            <option value="">Select District</option>
                            {districts.map((district, index) => (
                                <option key={index} value={district.name}>{district.name}</option>
                            ))}
                        </select>
                    ) : (
                        <p>Select State First</p>
                    )}

                    <label htmlFor="municipality">Municipality : </label>
                    <input type="text" required value={adminDetails.jurisdiction.municipality}
                    placeholder='Enter Municipality'
                    onChange={(e) => setAdminDetails({ ...adminDetails, jurisdiction: { ...adminDetails.jurisdiction, municipality: e.target.value } })} />

                </form>
            </section>
            <section>

            </section>
        </aside>
    </div>
  )
}

export default AdminMenege