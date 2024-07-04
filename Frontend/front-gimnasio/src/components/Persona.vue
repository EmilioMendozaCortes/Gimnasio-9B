<template>
    <div id="accordion-arrow-icon" data-accordion="open">
        <h2 id="accordion-arrow-icon-heading-2">
            <button type="button"
                class="flex items-center justify-between w-full p-5 font-medium rtl:text-right text-gray-500 border border-b-0 border-gray-200 focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-800 dark:border-gray-700 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800 gap-3"
                data-accordion-target="#accordion-arrow-icon-body-2" aria-expanded="false"
                aria-controls="accordion-arrow-icon-body-2">
                <span>Datos personales</span>
                <svg class="w-4 h-4 shrink-0 -me-0.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none"
                    viewBox="0 0 20 20">
                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M7.529 7.988a2.502 2.502 0 0 1 5 .191A2.441 2.441 0 0 1 10 10.582V12m-.01 3.008H10M19 10a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z" />
                </svg>
            </button>
        </h2>
        <div id="accordion-arrow-icon-body-2" class="hidden" aria-labelledby="accordion-arrow-icon-heading-2">
            <div class="p-5 border border-b-0 border-gray-200 dark:border-gray-700">
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
                <br>
            </div>
        </div>
        <h2 id="accordion-arrow-icon-heading-1">
            <button type="button"
                class="flex items-center justify-between w-full p-5 font-medium rtl:text-right text-gray-900 bg-gray-100 border border-b-0 border-gray-200 rounded-t-xl focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-800 dark:border-gray-700 dark:text-white dark:bg-gray-800 hover:bg-gray-100 dark:hover:bg-gray-800 gap-3"
                data-accordion-target="#accordion-arrow-icon-body-1" aria-expanded="true"
                aria-controls="accordion-arrow-icon-body-1">
                <span>Lista de personas</span>
            </button>
        </h2>
        <div id="accordion-arrow-icon-body-1" aria-labelledby="accordion-arrow-icon-heading-1">
            <div class="p-5 border border-b-0 border-gray-200 dark:border-gray-700 dark:bg-gray-900">
                <ListaPersona></ListaPersona>
            </div>
        </div>
    </div>

</template>

<script>
import ListaPersona from './ListaPersona.vue'
export default {
    components: [
        ListaPersona
    ],
    components: { ListaPersona }
}
</script>