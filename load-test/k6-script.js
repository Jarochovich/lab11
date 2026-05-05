import http from 'k6/http';
import { sleep } from 'k6';

export const options = {
  vus: 10,          // 10 виртуальных пользователей
  duration: '30s',  // Тест длится 30 секунд
};

export default function () {
  const res = http.get('http://localhost:3000');
  console.log(`Response time: ${res.timings.duration}ms`);
  sleep(1);
}