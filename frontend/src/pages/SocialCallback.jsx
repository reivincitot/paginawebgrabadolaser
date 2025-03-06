import { useEffect } from "react";
import { useNavigate } from "react-router-dom";


const SocialCallback = () => {
	const navigate = useNavigate();

	useEffect(() => {
		const params = new URLSearchParams(window.location.search);
		const accessToken = params.get("access");
		const refreshToken = params.get("refresh");

		if (accessToken && refreshToken) {
			localStorage.setItem("accessToken", accessToken);
			localStorage.setItem("refreshToken", refreshToken);
			navigate("/profile");
	} else {
		navigate("/login");
	}

	}
	, [navigate]);
	return (
		<div className="p-4 text-center">
			<p>Processing authentication...</p>
		</div>
	);
};

export default SocialCallback;