import React from 'react';

function UserProfile({ user }) {
  return (
    <div>
      <h2>{user.username}</h2>
      <p>Email: {user.email}</p>
    </div>
  );
}

export default UserProfile;
