import React from 'react';
import { Link } from 'react-router-dom';


const Header = () => {
  return (
    <header className='bg-blue-600 text-white p-4 shadow-md'>
      <div className='container mx-auto flex justify-between items.center'>
        <Link to="/" className='text-2x1 font-bold'>Grabados Láser 8102 GyP</Link>
        <nav>
          <ul className='flex space-x-4'>
            <li>
              <Link to="/catalog" className='hover:text-blue-200'>Catalog</Link>
            </li>
            <li>
              <Link to="/cart" className='hover:text-blue-200'>Cart</Link>
            </li>
            <li>
              <Link to="/profile" className='hover:text-blue-200'>Profile</Link>
            </li>
            <li>
              <Link to="/login" className='hover:text-blue-200'>Login</Link>
            </li>
          </ul>
        </nav>
      </div>
    </header>
  )
};

export default Header;