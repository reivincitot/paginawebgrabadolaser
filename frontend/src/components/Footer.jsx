// src/components/Footer.jsx
import React from 'react';
import { Link } from 'react-router-dom';

const Footer = () => {
  return (
    <footer className="bg-gray-800 text-white py-6 mt-8">
      <div className="container mx-auto px-4">
        <div className="flex flex-col md:flex-row justify-between items-center">
          {/* Sección del logo o nombre del sitio */}
          <div className="mb-4 md:mb-0">
            <Link to="/" className="text-2xl font-bold hover:text-gray-300">
              Grabados Láser 8102 GyP
            </Link>
          </div>
          {/* Menú de navegación */}
          <div className="mb-4 md:mb-0">
            <ul className="flex flex-wrap justify-center space-x-4">
              <li>
                <Link to="/catalog" className="hover:text-gray-300">Catalog</Link>
              </li>
              <li>
                <Link to="/cart" className="hover:text-gray-300">Cart</Link>
              </li>
              <li>
                <Link to="/profile" className="hover:text-gray-300">Profile</Link>
              </li>
              <li>
                <Link to="/dashboard" className="hover:text-gray-300">Dashboard</Link>
              </li>
            </ul>
          </div>
          {/* Redes sociales */}
          <div className="flex space-x-4">
            <a 
              href="https://facebook.com" 
              target="_blank" 
              rel="noopener noreferrer" 
              className="hover:text-gray-300"
            >
              {/* Icono de Facebook */}
              <svg className="w-6 h-6 fill-current" viewBox="0 0 24 24">
                <path d="M22.675,0H1.325C0.593,0,0,0.593,0,1.325v21.351C0,23.406,0.593,24,1.325,24H12.82v-9.294H9.692v-3.622h3.128V8.413
                  c0-3.1,1.893-4.788,4.659-4.788c1.325,0,2.464,0.099,2.794,0.143v3.24l-1.918,0.001c-1.504,0-1.796,0.715-1.796,1.763v2.313h3.587
                  l-0.467,3.622h-3.12V24h6.116C23.406,24,24,23.406,24,22.676V1.325C24,0.593,23.406,0,22.675,0z"/>
              </svg>
            </a>
            <a 
              href="https://instagram.com" 
              target="_blank" 
              rel="noopener noreferrer" 
              className="hover:text-gray-300"
            >
              {/* Icono de Instagram */}
              <svg className="w-6 h-6 fill-current" viewBox="0 0 24 24">
                <path d="M12,2.163c3.204,0,3.584,0.012,4.85,0.07c1.366,0.062,2.633,0.336,3.608,1.311c0.975,0.975,1.249,2.242,1.311,3.608
                  c0.058,1.266,0.069,1.645,0.069,4.85s-0.012,3.584-0.069,4.85c-0.062,1.366-0.336,2.633-1.311,3.608
                  c-0.975,0.975-2.242,1.249-3.608,1.311c-1.266,0.058-1.645,0.069-4.85,0.069s-3.584-0.012-4.85-0.069
                  c-1.366-0.062-2.633-0.336-3.608-1.311c-0.975-0.975-1.249-2.242-1.311-3.608C2.175,15.747,2.163,15.368,2.163,12
                  s0.012-3.584,0.07-4.85c0.062-1.366,0.336-2.633,1.311-3.608C4.52,2.499,5.787,2.225,7.153,2.163C8.419,2.105,8.799,2.093,12,2.093
                  M12,0C8.741,0,8.332,0.015,7.052,0.072C5.771,0.129,4.66,0.416,3.678,1.399C2.695,2.382,2.409,3.492,2.352,4.773
                  C2.295,6.053,2.28,6.463,2.28,9.722s0.015,3.669,0.072,4.949c0.057,1.281,0.344,2.391,1.327,3.374
                  c0.983,0.983,2.093,1.27,3.374,1.327C8.332,23.985,8.741,24,12,24s3.669-0.015,4.949-0.072
                  c1.281-0.057,2.391-0.344,3.374-1.327c0.983-0.983,1.27-2.093,1.327-3.374C23.985,13.391,24,12.981,24,9.722
                  s-0.015-3.669-0.072-4.949c-0.057-1.281-0.344-2.391-1.327-3.374C21.34,0.416,20.23,0.129,18.949,0.072
                  C17.669,0.015,17.259,0,14,0H12z M12,5.838c-3.403,0-6.162,2.759-6.162,6.162S8.597,18.162,12,18.162
                  s6.162-2.759,6.162-6.162S15.403,5.838,12,5.838 M12,16.162c-2.208,0-4-1.792-4-4s1.792-4,4-4s4,1.792,4,4
                  S14.208,16.162,12,16.162 M18.406,4.594c-0.796,0-1.44,0.644-1.44,1.44c0,0.796,0.644,1.44,1.44,1.44
                  s1.44-0.644,1.44-1.44C19.846,5.238,19.202,4.594,18.406,4.594z"/>
              </svg>
            </a>
            <a 
              href="https://twitter.com" 
              target="_blank" 
              rel="noopener noreferrer" 
              className="hover:text-gray-300"
            >
              {/* Icono de Twitter */}
              <svg className="w-6 h-6 fill-current" viewBox="0 0 24 24">
                <path d="M24,4.557c-0.883,0.392-1.832,0.656-2.828,0.775c1.017-0.609,1.798-1.574,2.165-2.723c-0.951,0.564-2.005,0.974-3.127,1.195
                C19.64,2.924,18.356,2.4,17,2.4c-2.905,0-5.26,2.355-5.26,5.26c0,0.413,0.046,0.816,0.135,1.203C7.728,8.132,4.1,6.13,1.671,3.149
                C1.247,3.878,1.007,4.705,1.007,5.574c0,1.823,0.928,3.431,2.337,4.376c-0.861-0.027-1.672-0.264-2.379-0.657v0.066
                c0,2.546,1.811,4.667,4.212,5.148c-0.441,0.12-0.905,0.184-1.384,0.184c-0.338,0-0.666-0.033-0.988-0.094
                c0.666,2.079,2.601,3.593,4.897,3.634c-1.794,1.405-4.05,2.244-6.506,2.244c-0.423,0-0.84-0.025-1.253-0.074
                C2.927,21.29,6.404,22,10.073,22c12.074,0,18.675-10.002,18.675-18.675c0-0.285-0.006-0.568-0.019-0.85
                C22.505,6.411,23.34,5.543,24,4.557z"/>
              </svg>
            </a>
          </div>
        </div>
        <div className="mt-4 border-t pt-4 text-center text-sm text-gray-400">
          <p>&copy; {new Date().getFullYear()} Grabados Láser 8102 GyP. All rights reserved.</p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
