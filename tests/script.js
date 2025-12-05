import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  vus: 10,
  duration: '10s',
};
export default function () {
  
  const payload = JSON.stringify({
    user_id: Math.floor(Math.random() * 100) + 1,
    event_id: 1,
  });

  const params = {
    headers: {
      'Content-Type': 'application/json',
    },
  };

  const res = http.post('http://api:8000/bookings/', payload, params);

  check(res, {
    'is status 200 or 400': (r) => r.status === 200 || r.status === 400,
  });

  sleep(1);
}