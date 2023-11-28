import { createClient, print} from 'redis';
import { promisify } from 'util';

const client = createClient();

// promisify Redis cleint methods
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

client.on('error', (err) => {
  console.log(
  'Redis client not connected to the server:', err.toString());
});

client.on('connect', () => {
  console.log('Redis client connectd to the server');
});

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, print);
};


const displaySchoolValue = async (schoolName) => {
  try {
    const result = await getAsync(schoolName);
    console.log(result);
  } catch (error) {
    console.error('Error:', error);
  } finally {
  }
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
