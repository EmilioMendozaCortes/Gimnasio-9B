<template>
    <div class="grid gap-8">
            <div id="back-div" class="bg-gradient-to-r from-blue-500 to-purple-500 rounded-[26px] m-4 ">
                <div
                    class="border-[20px] border-transparent rounded-[20px] dark:bg-gray-900 bg-white shadow-lg xl:p-10 2xl:p-10 lg:p-10 md:p-10 sm:p-2 m-2">
                    <h1 class="pt-8 pb-6 font-bold text-5xl dark:text-gray-400 text-center cursor-default">
                        Registrar Usuario
                    </h1>
                    <h4 class="pt-8 pb-6 font-bold text-3xl dark:text-gray-400 text-center cursor-default">
                        Datos personales
                    </h4>
                    <form action="#" method="post" class="space-y-4">
                        <div>
                            <label for="nombre" class="mb-2 dark:text-gray-400 text-lg">Nombre</label>
                            <input id="nombre"
                                class="border dark:bg-indigo-700 dark:text-gray-300 dark:border-gray-700 p-3 shadow-md placeholder:text-base border-gray-300 rounded-lg w-full focus:scale-105 ease-in-out duration-300"
                                type="text" placeholder="Nombre" required />
                        </div>
                        <div>
                            <label for="primer apellido" class="mb-2 dark:text-gray-400 text-lg">Primer apellido</label>
                            <input id="primerApellido"
                                class="border dark:bg-indigo-700 dark:text-gray-300 dark:border-gray-700 p-3 shadow-md placeholder:text-base border-gray-300 rounded-lg w-full focus:scale-105 ease-in-out duration-300"
                                type="text" placeholder="Primer apellido" required />
                        </div>
                        <div>
                            <label for="segundo apellido" class="mb-2 dark:text-gray-400 text-lg">Segundo apellido</label>
                            <input id="segundoApellido"
                                class="border dark:bg-indigo-700 dark:text-gray-300 dark:border-gray-700 p-3 shadow-md placeholder:text-base border-gray-300 rounded-lg w-full focus:scale-105 ease-in-out duration-300"
                                type="text" placeholder="Segundo apellido" required />
                        </div>
                        <div>
                            <label for="titulo de cortesia" class="mb-2 dark:text-gray-400 text-lg">Titulo de cortesia</label>
                            <input id="TtituloDeCortesia"
                                class="border dark:bg-indigo-700 dark:text-gray-300 dark:border-gray-700 p-3 shadow-md placeholder:text-base border-gray-300 rounded-lg w-full focus:scale-105 ease-in-out duration-300"
                                type="text" placeholder="Titulo de cortesia" required />
                        </div>
                        <div>
                            <label for="foto" class="mb-2 dark:text-gray-400 text-lg">Foto</label> <br>
                            <input id="foto"
                                class="border dark:bg-indigo-700 dark:text-gray-300 dark:border-gray-700 p-3 shadow-md placeholder:text-base border-gray-300 rounded-lg w-full focus:scale-105 ease-in-out duration-300"
                                type="file" placeholder="Foto" required />
                        </div>
                        <div>
                            <label for="genero" class="mb-2 dark:text-gray-400 text-lg">Genero</label>
                            <select name="genero">
                                <option value="" disabled>Seleccione un genero</option>
                                <option value="a+">Masculino</option>
                                <option value="a-">Femenino</option>
                            </select>
                        </div>
                        <div>
                            <label for="sangre" class="mb-2 dark:text-gray-400 text-lg">Tipo de sangre</label>
                            <select name="sangre">
                                <option value="" disabled>Seleccione un tipo de sangre</option>
                                <option value="a+">A+</option>
                                <option value="a-">A-</option>
                                <option value="b+">B+</option>
                                <option value="b-">B-</option>
                                <option value="ab+">AB+</option>
                                <option value="ab-">AB-</option>
                                <option value="o+">O+</option>
                                <option value="o-">O-</option>
                            </select>
                        </div>
                        <div>
                            <label for="fechaNacimiento" class="mb-2 dark:text-gray-400 text-lg">Fecha de Nacimiento</label>
                            <input id="fechaNacimiento"
                                class="border dark:bg-indigo-700 dark:text-gray-300 dark:border-gray-700 p-3 shadow-md placeholder:text-base border-gray-300 rounded-lg w-full focus:scale-105 ease-in-out duration-300"
                                type="date" placeholder="Fecha de Nacimiento" required />
                        </div>
                        
                        <button
                            class="bg-gradient-to-r from-blue-500 to-purple-500 shadow-lg mt-6 p-2 text-white rounded-lg w-full hover:scale-105 hover:from-purple-500 hover:to-blue-500 transition duration-300 ease-in-out"
                            type="submit">
                            Registrarse
                        </button>
                    </form>
                    <div class="flex flex-col mt-4 items-center justify-center text-sm">
                        <h3>
                            <span class="cursor-default dark:text-gray-300">¿Ya tiene una cuenta?</span>
                            <a class="group text-blue-400 transition-all duration-100 ease-in-out" href="#">
                                <span
                                    class="bg-left-bottom ml-1 bg-gradient-to-r from-blue-400 to-blue-400 bg-[length:0%_2px] bg-no-repeat group-hover:bg-[length:100%_2px] transition-all duration-500 ease-out">
                                    Iniciar seción
                                </span>
                            </a>
                        </h3>
                    </div>

                    <!-- Third Party Authentication Options -->
                    <div id="third-party-auth" class="flex items-center justify-center mt-5 flex-wrap">
                        <button href="#" class="hover:scale-105 ease-in-out duration-300 shadow-lg p-2 rounded-lg m-1">
                            <img class="max-w-[25px]" src="https://ucarecdn.com/8f25a2ba-bdcf-4ff1-b596-088f330416ef/"
                                alt="Google" />
                        </button>
                        <button href="#" class="hover:scale-105 ease-in-out duration-300 shadow-lg p-2 rounded-lg m-1">
                            <img class="max-w-[25px]" src="https://ucarecdn.com/95eebb9c-85cf-4d12-942f-3c40d7044dc6/"
                                alt="Linkedin" />
                        </button>
                        <button href="#" class="hover:scale-105 ease-in-out duration-300 shadow-lg p-2 rounded-lg m-1">
                            <img class="max-w-[25px] filter dark:invert"
                                src="https://ucarecdn.com/be5b0ffd-85e8-4639-83a6-5162dfa15a16/" alt="Github" />
                        </button>
                        <button href="#" class="hover:scale-105 ease-in-out duration-300 shadow-lg p-2 rounded-lg m-1">
                            <img class="max-w-[25px]" src="https://ucarecdn.com/6f56c0f1-c9c0-4d72-b44d-51a79ff38ea9/"
                                alt="Facebook" />
                        </button>
                        <button href="#" class="hover:scale-105 ease-in-out duration-300 shadow-lg p-2 rounded-lg m-1">
                            <img class="max-w-[25px] dark:gray-100"
                                src="https://ucarecdn.com/82d7ca0a-c380-44c4-ba24-658723e2ab07/" alt="twitter" />
                        </button>

                        <button href="#" class="hover:scale-105 ease-in-out duration-300 shadow-lg p-2 rounded-lg m-1">
                            <img class="max-w-[25px]" src="https://ucarecdn.com/3277d952-8e21-4aad-a2b7-d484dad531fb/"
                                alt="apple" />
                        </button>
                    </div>
                    <div class="text-gray-500 flex text-center flex-col mt-4 items-center text-sm">
                        <p class="cursor-default">
                            Al iniciar seción, aceptas nuestros
                            <a class="group text-blue-400 transition-all duration-100 ease-in-out" href="#">
                                <span
                                    class="cursor-pointer bg-left-bottom bg-gradient-to-r from-blue-400 to-blue-400 bg-[length:0%_2px] bg-no-repeat group-hover:bg-[length:100%_2px] transition-all duration-500 ease-out">
                                    Terminos
                                </span>
                            </a>
                            y
                            <a class="group text-blue-400 transition-all duration-100 ease-in-out" href="#">
                                <span
                                    class="cursor-pointer bg-left-bottom bg-gradient-to-r from-blue-400 to-blue-400 bg-[length:0%_2px] bg-no-repeat group-hover:bg-[length:100%_2px] transition-all duration-500 ease-out">
                                    Política de Privacidad
                                </span>
                            </a>
                            de Bull's Gym
                        </p>
                    </div>
                </div>
            </div>
        </div>
</template>