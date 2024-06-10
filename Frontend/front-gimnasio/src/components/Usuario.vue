<template>
    <div class="grid gap-8">
            <div id="back-div" class="bg-gradient-to-r from-blue-500 to-purple-500 rounded-[26px] m-4 ">
                <div
                    class="border-[20px] border-transparent rounded-[20px] dark:bg-gray-900 bg-white shadow-lg xl:p-10 2xl:p-10 lg:p-10 md:p-10 sm:p-2 m-2">
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
                    </form>
                   

                    
                </div>
            </div>
        </div>
</template>