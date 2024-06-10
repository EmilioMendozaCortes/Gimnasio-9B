<template>
    <form action="#" method="post" class="space-y-4">
        <div>
            <label for="usuario" class="mb-2 dark:text-gray-400 text-lg">Usuario</label>
            <input id="usuario"
                class="border dark:bg-indigo-700 dark:text-gray-300 dark:border-gray-700 p-3 mb-2 shadow-md placeholder:text-base border-gray-300 rounded-lg w-full focus:scale-105 ease-in-out duration-300"
                type="text" placeholder="Usuario" required />
        </div>
        <div>
            <label for="password" class="mb-2 dark:text-gray-400 text-lg">Contraseña</label>
            <input id="password"
                class="border dark:bg-indigo-700 dark:text-gray-300 dark:border-gray-700 p-3 mb-2 shadow-md placeholder:text-base border-gray-300 rounded-lg w-full focus:scale-105 ease-in-out duration-300"
                type="password" placeholder="Contraseña" required />
        </div>
        <div>
            <label for="password2" class="mb-2 dark:text-gray-400 text-lg">Repetir Contraseña</label>
            <input id="password2"
                class="border dark:bg-indigo-700 dark:text-gray-300 dark:border-gray-700 p-3 mb-2 shadow-md placeholder:text-base border-gray-300 rounded-lg w-full focus:scale-105 ease-in-out duration-300"
                type="password" placeholder="Repetir Contraseña" required />
        </div>
    </form>
</template>