import time
import psutil
from user_management import UserManagement, UserAlreadyExistsError, UserNotFoundError, InvalidPasswordError

def benchmark_user_management():
    um = UserManagement()
    process = psutil.Process()
    
    # Benchmark user registration
    start_time = time.time()
    try:
        um.register_user('testuser', 'testuser@example.com', 'password')
    except UserAlreadyExistsError:
        pass
    end_time = time.time()
    register_time = end_time - start_time
    register_memory = process.memory_info().rss / (1024 ** 2)  # Convert to MB
    
    # Benchmark user login
    start_time = time.time()
    try:
        um.login_user('testuser', 'password')
    except (UserNotFoundError, InvalidPasswordError):
        pass
    end_time = time.time()
    login_time = end_time - start_time
    login_memory = process.memory_info().rss / (1024 ** 2)  # Convert to MB
    
    # Benchmark get user info
    start_time = time.time()
    try:
        um.get_user_info('testuser')
    except UserNotFoundError:
        pass
    end_time = time.time()
    get_info_time = end_time - start_time
    get_info_memory = process.memory_info().rss / (1024 ** 2)  # Convert to MB
    
    # Print benchmark results
    print(f"User registration time: {register_time:.6f} seconds")
    print(f"User registration memory: {register_memory:.2f} MB")
    
    print(f"User login time: {login_time:.6f} seconds")
    print(f"User login memory: {login_memory:.2f} MB")
    
    print(f"Get user info time: {get_info_time:.6f} seconds")
    print(f"Get user info memory: {get_info_memory:.2f} MB")

if __name__ == "__main__":
    benchmark_user_management()

